#!/bin/sh
set -e
cd "$(dirname "$0")"
(cd code && python3 -m unittest discover -s tests)
echo "all tests passed"
