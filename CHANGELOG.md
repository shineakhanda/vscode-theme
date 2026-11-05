# Changelog

## 1.1.0 — 2026-11-06
- Theme is now a real installable extension (`package.json` + `.vsix`) instead of a loose JSON file.
- Full workbench palette (tabs, panels, terminal ANSI, git decorations, diff, brackets) and semantic highlighting.
- Fixed invalid `extensions.json` (duplicated closing block, junk entry `wix.glean`); removed redundant `redhat.java`, `twxs.cmake`, `ms-dotnettools.vscode-dotnet-runtime` (already pulled in by their packs).
- One-command extension installers for macOS/Linux and Windows.
- Settings: removed obsolete `files.maxMemoryForLargeFilesMB`, fixed `editor.cursorSmoothCaretAnimation`, added default formatters and ESLint fix-on-save.
- Snippets bundled in the extension; added React, fetch, try/catch, grid and media-query snippets.
- Rebranded from Cave Web Solution to Cave Technologies.

## 1.0.0
- Initial release as Cave Web Solution setup.
