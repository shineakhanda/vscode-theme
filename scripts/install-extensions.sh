#!/usr/bin/env bash
# Installs every extension listed in extensions.json (macOS / Linux / Git Bash).
# Usage:  ./scripts/install-extensions.sh            install all
#         ./scripts/install-extensions.sh --web      web-development group only
set -euo pipefail
cd "$(dirname "$0")/.."

if ! command -v code >/dev/null 2>&1; then
  echo "✖ 'code' command not found."
  echo "  In VS Code: Ctrl/Cmd+Shift+P → 'Shell Command: Install code command in PATH', then re-run."
  exit 1
fi

# Strip // comments, then pull out quoted extension IDs
ids=$(sed 's#//.*##' extensions.json | grep -oE '"[A-Za-z0-9-]+\.[A-Za-z0-9.-]+"' | tr -d '"')
if [[ "${1:-}" == "--web" ]]; then
  ids=$(sed -n '/Web development/,/Java/p' extensions.json | sed 's#//.*##' | grep -oE '"[A-Za-z0-9-]+\.[A-Za-z0-9.-]+"' | tr -d '"')
fi

installed=$(code --list-extensions | tr '[:upper:]' '[:lower:]')
for id in $ids; do
  if grep -qx "$(echo "$id" | tr '[:upper:]' '[:lower:]')" <<<"$installed"; then
    echo "✔ $id (already installed)"
  else
    echo "→ installing $id"
    code --install-extension "$id" --force >/dev/null || echo "✖ failed: $id"
  fi
done
echo "Done."
