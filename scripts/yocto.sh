#!/bin/bash
set -e
case "$1" in build) echo build ;; clean) echo clean ;; package) echo package ;; sbom) echo sbom ;; *) echo usage; exit 1;; esac