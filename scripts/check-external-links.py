"""Bounded HTTP checks of authored external links; access restrictions are reported separately."""
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
from ipaddress import ip_address
from urllib.parse import urlsplit, urlunsplit, quote
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
import argparse
import json
import ssl
import threading

locks = {}
guard = threading.Lock()

def check(record, context=None):
    original = record["url"]
    parts = urlsplit(original)
    host = (parts.hostname or "").lower()
    local = host == "localhost" or host.endswith((".localhost", ".local", ".test", ".invalid", ".example")) or any(
        host == name or host.endswith("." + name) for name in ("example.com", "example.org", "example.net"))
    try:
        local = local or not ip_address(host).is_global
    except ValueError:
        pass  # A DNS hostname is not an IP literal.
    if local:
        return {**record, "status": "example-or-local", "http_status": None, "final_url": original,
                "error": "Example or local-service URL; not probed as an external destination."}
    url = urlunsplit((parts.scheme,parts.netloc,quote(parts.path,safe="/%:@-._~!$&'()*+,;="),quote(parts.query,safe="=&%/:?@-._~!$'()*+,;"),""))
    with guard:
        gate=locks.setdefault(parts.netloc,threading.BoundedSemaphore(2))
    with gate:
        code=None
        final=url
        error=None
        for method in ["HEAD","GET"]:
            code=None
            final=url
            try:
                request=Request(url,method=method,headers={"User-Agent":"Mozilla/5.0 (compatible; DeveloperLibraryLinkCheck/1.0)"})
                with urlopen(request,timeout=10,context=context) as response:
                    code=response.status
                    final=response.url
                error=None
                break
            except HTTPError as problem:
                code=problem.code
                final=problem.url
                error=str(problem)
                problem.close()
                if method=="HEAD":continue
                break
            except (URLError,TimeoutError,OSError,ValueError) as problem:
                error=str(problem)
                if method=="HEAD":continue
                break
        status="reachable" if code and 200<=code<400 else "not-found" if code in [404,410] else "restricted-or-transient"
        return {**record,"status":status,"http_status":code,"final_url":final,"error":error}

if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input",type=Path)
    parser.add_argument("--report",type=Path,required=True)
    parser.add_argument("--native-tls",action="store_true",
                        help="Use the operating system certificate store through the optional truststore package; TLS verification stays enabled.")
    parser.add_argument("--strict",action="store_true",
                        help="Also fail when any public destination remains unverified.")
    args=parser.parse_args()
    context=None
    if args.native_tls:
        try:
            import truststore
        except ModuleNotFoundError:
            parser.error("--native-tls requires truststore; install it with python -m pip install truststore")
        context=truststore.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    records=json.loads(args.input.read_text(encoding="utf-8"))
    results=[]
    with ThreadPoolExecutor(max_workers=16) as pool:
        futures=[pool.submit(check,record,context) for record in records]
        for future in as_completed(futures):
            results.append(future.result())
            if len(results)%100==0:print(f"Checked {len(results)}/{len(records)}",flush=True)
    results.sort(key=lambda item:item["url"])
    summary=dict(Counter(item["status"] for item in results))
    report={"checked_on":datetime.now(timezone.utc).isoformat(),"summary":summary,
            "tls":"native certificate store" if args.native_tls else "Python default certificate store",
            "strict":args.strict,
            "limits":"HTTP availability only; fragments and documentation accuracy are not verified. 403/429, TLS/network failures and server errors require manual review. Internal source and publication targets are checked locally.","links":results}
    args.report.parent.mkdir(parents=True,exist_ok=True)
    args.report.write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(summary,indent=2))
    raise SystemExit(1 if summary.get("not-found", 0) else 2 if args.strict and summary.get("restricted-or-transient", 0) else 0)
