"""Bounded HTTP checks of authored external links; access restrictions are reported separately."""
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from collections import Counter
from urllib.parse import urlsplit, urlunsplit, quote
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
import argparse
import json
import ssl
import threading

locks = {}
guard = threading.Lock()

def check(record):
    original = record["url"]
    parts = urlsplit(original)
    url = urlunsplit((parts.scheme,parts.netloc,quote(parts.path,safe="/%:@-._~!$&'()*+,;="),quote(parts.query,safe="=&%/:?@-._~!$'()*+,;"),""))
    with guard:
        gate=locks.setdefault(parts.netloc,threading.BoundedSemaphore(2))
    with gate:
        code=None
        final=url
        error=None
        for method in ["HEAD","GET"]:
            try:
                request=Request(url,method=method,headers={"User-Agent":"Mozilla/5.0 (compatible; DeveloperLibraryLinkCheck/1.0)","Range":"bytes=0-1023"})
                with urlopen(request,timeout=10) as response:
                    code=response.status
                    final=response.url
                error=None
                break
            except HTTPError as problem:
                code=problem.code
                final=problem.url
                error=str(problem)
                if method=="HEAD" and code in [400,403,404,405,429,500,502,503]:continue
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
    args=parser.parse_args()
    records=json.loads(args.input.read_text(encoding="utf-8"))
    results=[]
    with ThreadPoolExecutor(max_workers=16) as pool:
        futures=[pool.submit(check,record) for record in records]
        for future in as_completed(futures):
            results.append(future.result())
            if len(results)%100==0:print(f"Checked {len(results)}/{len(records)}",flush=True)
    results.sort(key=lambda item:item["url"])
    summary=dict(Counter(item["status"] for item in results))
    report={"checked_on":"2026-10-28","summary":summary,"limits":"HTTP availability only; fragments and documentation accuracy are not verified. 403/429, network failures and server errors require manual review. Planned destination repository/site URLs are excluded.","links":results}
    args.report.parent.mkdir(parents=True,exist_ok=True)
    args.report.write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(summary,indent=2))
