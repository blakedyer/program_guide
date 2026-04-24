#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT_DIR"

python3 scripts/build_static_site.py

if [[ -n "$(git status --porcelain)" ]]; then
  echo "There are uncommitted changes. Commit them first, then rerun this script to push the current branch."
  exit 1
fi

BRANCH="$(git branch --show-current)"
git push -u origin "$BRANCH"

echo "Pushed ${BRANCH}. GitHub Actions will rebuild and deploy GitHub Pages from the latest commit."
