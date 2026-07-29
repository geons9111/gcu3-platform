#!/usr/bin/env python3

import argparse
import subprocess
import sys


def run_build():
    print("[GCU3] build requested")
    print("[INFO] build-wayland wrapper (Phase1)")


def run_clean():
    print("[GCU3] clean requested")


def run_package():
    print("[GCU3] package requested")


def run_sbom():
    print("[GCU3] sbom requested")


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "command",
        choices=[
            "build",
            "clean",
            "package",
            "sbom"
        ]
    )

    args = parser.parse_args()

    if args.command == "build":
        run_build()

    elif args.command == "clean":
        run_clean()

    elif args.command == "package":
        run_package()

    elif args.command == "sbom":
        run_sbom()


if __name__ == "__main__":
    sys.exit(main())