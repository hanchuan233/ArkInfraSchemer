from __future__ import annotations

import argparse
import json

from backend.app.api import generate_schedule_api


def main() -> None:
    parser = argparse.ArgumentParser(description="ArkInfraSchemer V1 scheduler CLI")
    parser.add_argument("--layout", default="252", choices=["252", "243"])
    parser.add_argument("--top-k", type=int, default=3)
    parser.add_argument("--ops", nargs="+", required=True, help="owned operator ids")
    args = parser.parse_args()

    payload = {
        "layout": args.layout,
        "top_k": args.top_k,
        "owned_operator_ids": args.ops,
    }
    print(json.dumps(generate_schedule_api(payload), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
