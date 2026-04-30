#!/usr/bin/env python3
"""MinerU API test client. Usage: python test_client.py <file_path> [--async]"""

import argparse
import json
import time
import requests

BASE_URL = "http://174.15.0.58:9000"


def health_check():
    r = requests.get(f"{BASE_URL}/health")
    r.raise_for_status()
    print("Health:", json.dumps(r.json(), indent=2))
    return r.json()["status"] == "healthy"


def sync_parse(file_path, backend="pipeline"):
    print(f"Sync parsing: {file_path} (backend={backend})")
    with open(file_path, "rb") as f:
        r = requests.post(
            f"{BASE_URL}/file_parse",
            files={"files": (file_path, f)},
            data={"backend": backend, "return_md": "true"},
        )
    r.raise_for_status()
    result = r.json()
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return result


def async_parse(file_path, backend="pipeline", poll_interval=3):
    print(f"Async parsing: {file_path} (backend={backend})")
    with open(file_path, "rb") as f:
        r = requests.post(
            f"{BASE_URL}/tasks",
            files={"files": (file_path, f)},
            data={"backend": backend, "return_md": "true"},
        )
    r.raise_for_status()
    task = r.json()
    task_id = task["task_id"]
    print(f"Task submitted: {task_id}")

    while True:
        time.sleep(poll_interval)
        status = requests.get(f"{BASE_URL}/tasks/{task_id}").json()
        state = status.get("state", status.get("status"))
        print(f"  Status: {state}")
        if state in ("done", "completed", "success"):
            break
        if state in ("failed", "error"):
            print("Task failed:", json.dumps(status, indent=2))
            return status

    r = requests.get(f"{BASE_URL}/tasks/{task_id}/result")
    r.raise_for_status()
    result = r.json()
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MinerU API test client")
    parser.add_argument("file", help="File to parse (PDF, image, DOCX, PPTX, XLSX)")
    parser.add_argument("--async", dest="use_async", action="store_true", help="Use async task API")
    parser.add_argument("--backend", default="pipeline", help="Backend: pipeline, vlm-auto-engine, hybrid-auto-engine, etc.")
    args = parser.parse_args()

    if not health_check():
        print("Service unhealthy, aborting.")
        exit(1)

    print("---")
    if args.use_async:
        async_parse(args.file, backend=args.backend)
    else:
        sync_parse(args.file, backend=args.backend)
