"""Network-free regression checks for external-link classification."""
import importlib.util
import io
import json
from pathlib import Path
import runpy
import sys
import tempfile
from unittest import TestCase, main
from unittest.mock import MagicMock, patch
from urllib.error import HTTPError, URLError

spec = importlib.util.spec_from_file_location(
    "external_links", Path(__file__).resolve().parents[1] / "scripts/check-external-links.py")
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class ExternalLinkTests(TestCase):
    def test_examples_and_local_services_are_not_requested(self):
        with patch.object(checker, "urlopen") as request:
            for url in ["http://localhost:8080", "http://127.0.0.1", "http://[::1]",
                        "https://example.com", "https://api.example.org", "https://host.test"]:
                self.assertEqual(checker.check({"url": url})["status"], "example-or-local")
            request.assert_not_called()

    def test_failed_get_does_not_reuse_a_head_404(self):
        url = "https://docs.python.org/missing"
        with patch.object(checker, "urlopen", side_effect=[
            HTTPError(url, 404, "HEAD not found", {}, None), URLError("TLS verification failed")
        ]):
            result = checker.check({"url": url})
        self.assertEqual(result["status"], "restricted-or-transient")
        self.assertIsNone(result["http_status"])

    def test_get_confirms_missing_or_successful_destination(self):
        url = "https://docs.python.org/missing"
        with patch.object(checker, "urlopen", side_effect=[
            HTTPError(url, 404, "HEAD not found", {}, None),
            HTTPError(url, 404, "GET not found", {}, None)
        ]):
            self.assertEqual(checker.check({"url": url})["status"], "not-found")
        response = MagicMock()
        response.__enter__.return_value.status = 200
        response.__enter__.return_value.url = url
        with patch.object(checker, "urlopen", side_effect=[
            HTTPError(url, 405, "HEAD unsupported", {}, None), response
        ]):
            self.assertEqual(checker.check({"url": url})["status"], "reachable")

    def test_supplied_native_context_is_used_for_certificate_verification(self):
        context = object()
        response = MagicMock()
        response.__enter__.return_value.status = 200
        response.__enter__.return_value.url = "https://docs.python.org/"
        with patch.object(checker, "urlopen", return_value=response) as request:
            self.assertEqual(checker.check({"url": "https://docs.python.org/"}, context)["status"], "reachable")
            self.assertIs(request.call_args.kwargs["context"], context)
            self.assertFalse(request.call_args.args[0].has_header("Range"))

    def test_strict_cli_rejects_unverified_requests_and_persists_the_reason(self):
        with tempfile.TemporaryDirectory() as directory:
            input_file = Path(directory) / "input.json"
            report_file = Path(directory) / "report.json"
            input_file.write_text(json.dumps([{"url": "https://docs.python.org/"}]))
            argv = [str(spec.origin), str(input_file), "--strict", "--report", str(report_file)]
            with patch.object(sys, "argv", argv), patch("urllib.request.urlopen", side_effect=URLError("TLS verification failed")), \
                    patch("sys.stdout", new_callable=io.StringIO), self.assertRaises(SystemExit) as result:
                runpy.run_path(spec.origin, run_name="__main__")
            self.assertEqual(result.exception.code, 2)
            report = json.loads(report_file.read_text())
            self.assertTrue(report["strict"])
            self.assertEqual(report["summary"], {"restricted-or-transient": 1})
            self.assertIn("TLS verification failed", report["links"][0]["error"])


if __name__ == "__main__":
    main()
