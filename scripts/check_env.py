#!/usr/bin/env python3
"""Read-only local Claude environment overview. Never print secrets or full IPs."""

from __future__ import annotations

import argparse
import json
import locale
import os
from pathlib import Path
import platform
import sys
import time
import urllib.request
from typing import Any

VARIABLES = (
    "ANTHROPIC_API_KEY",
    "ANTHROPIC_AUTH_TOKEN",
    "ANTHROPIC_BASE_URL",
    "HTTP_PROXY",
    "HTTPS_PROXY",
    "ALL_PROXY",
    "NO_PROXY",
)


def environment_summary(home: Path | None = None) -> dict[str, Any]:
    """Collect non-secret local configuration metadata; no network access."""
    home = home or Path.home()
    current_locale = locale.getlocale()
    return {
        "platform": platform.system(),
        "os_release": platform.release(),
        "python": platform.python_version(),
        "timezone_names": list(time.tzname),
        "utc_offset_hours": round(-time.timezone / 3600, 2),
        "locale": current_locale[0] or "not set",
        "variables_present": {name: name in os.environ for name in VARIABLES},
        "claude_paths_present": {
            ".claude": (home / ".claude").exists(),
            ".claude.json": (home / ".claude.json").exists(),
        },
        "note": "No secret values, cookies, or public IPs collected.",
    }


def network_summary(timeout: float = 6.0) -> dict[str, str]:
    """Opt-in public request. Report only region, HTTP status, and TLS scheme."""
    url = "https://www.cloudflare.com/cdn-cgi/trace"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "bobopig-claude-audit/1.0"})
        with urllib.request.urlopen(req, timeout=timeout) as response:
            # Do not return or store `ip=` from the response.
            payload = response.read(8192).decode("utf-8", errors="replace")
            entries = dict(
                line.split("=", 1) for line in payload.splitlines() if "=" in line
            )
            return {
                "result": "ok",
                "http_status": str(response.status),
                "country_code": entries.get("loc", "unavailable"),
                "tls": entries.get("tls", "unavailable"),
                "note": "Python process path only; not a Claude CLI/browser/WebRTC test.",
            }
    except Exception as exc:
        return {"result": "error", "kind": type(exc).__name__,
                "note": "Network lookup did not complete. No IP printed."}


def main() -> int:
    parser = argparse.ArgumentParser(description="Read-only Claude environment check")
    parser.add_argument("--network", action="store_true", help="Opt-in public country lookup")
    parser.add_argument("--json", action="store_true", help="Print JSON rather than labels")
    args = parser.parse_args()
    report: dict[str, Any] = environment_summary()
    if args.network:
        report["network"] = network_summary()
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print("Claude local environment (read-only; no secrets)")
        for key, value in report.items():
            if isinstance(value, dict):
                print(f"\n[{key}]")
                for name, item in value.items():
                    print(f"  {name}: {item}")
            else:
                print(f"{key}: {value}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
