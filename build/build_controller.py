#!/usr/bin/env python3

import argparse
import datetime
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

LOG_DIR = ROOT_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "build.log"


def log(message):
    timestamp = datetime.datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    line = f"[{timestamp}] {message}"

    print(line)

    with open(LOG_FILE, "a") as fp:
        fp.write(line + "\n")


def detect_build_wayland():
    candidates = [
        ROOT_DIR / "build-wayland",
        ROOT_DIR / "../build-wayland",
    ]

    for candidate in candidates:
        if candidate.exists():
            log(f"build-wayland found : {candidate}")
            return candidate

    log("build-wayland not found")
    return None


def run_build():
    log("build requested")

    detect_build_wayland()

    return 0


def run_clean():
    log("clean requested")
    return 0


def run_package():
    log("package requested")
    return 0


def run_sbom():
    log("sbom requested")
    return 0


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "command",
        choices=["build", "clean", "package", "sbom"]
    )

    args = parser.parse_args()

    if args.command == "build":
        return run_build()

    if args.command == "clean":
        return run_clean()

    if args.command == "package":
        return run_package()

    if args.command == "sbom":
        return run_sbom()

    return 1


if __name__ == "__main__":
    sys.exit(main())