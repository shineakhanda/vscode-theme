# 🦇 Cave Dark Pro · VS Code Setup by Shine

A clean, fast VS Code setup for web and multi-language development: a custom dark theme, ready-made snippets, tuned settings, handy shortcuts and a curated extension list you can install in one command.

Made and used daily by **Shine** ([@shineakhanda](https://github.com/shineakhanda)), founder of **Cave Technologies** — a Bangladesh-based digital agency for web development, business automation, custom CMS plugins and themes, and brand building. *(This project started life as the "Cave Web Solution" setup, Cave Technologies' earlier name.)*

---

## ✨ What's inside

| | What | File |
|---|---|---|
| 🎨 | **Cave Dark Pro** — eye-comfort dark theme with full UI + semantic highlighting | `themes/` (packaged as an extension) |
| ✂️ | **Snippets** for HTML, CSS/SCSS, JS/TS and React — bundled with the theme | `snippets/` |
| 🧩 | **37 curated extensions** grouped by language, with one-command installers | `extensions.json`, `scripts/` |
| ⚡ | **Tuned settings** — formatting on save, sensible excludes, JetBrains Mono | `settings.json` |
| ⌨️ | **Shortcuts** for editing, navigation, terminal, debugging and GitLens | `keybindings.json` |
| 🏢 | **Multi-root workspace** template | `workspace/cave.code-workspace` |

---

## 🚀 Quick start

You need [VS Code](https://code.visualstudio.com/), [Git](https://git-scm.com/) and [Node.js](https://nodejs.org/) (only for building the theme).

```bash
git clone https://github.com/shineakhanda/vscode-theme.git
cd vscode-theme
```

> **Make sure the `code` command works.** Run `code --version` in a terminal. If it isn't found:
> - **macOS:** in VS Code press `Cmd+Shift+P` → **Shell Command: Install 'code' command in PATH**.
> - **Windows:** reinstall VS Code with **Add to PATH** ticked, then open a new terminal.
> - **Linux:** it's installed with the `.deb`/`.rpm` package automatically.

### 1. Install the Cave Dark Pro theme + snippets

**Option A — download the ready-made file (easiest)**
1. Open the [Releases](https://github.com/shineakhanda/vscode-theme/releases) page and download `cave-dark-pro-x.x.x.vsix`.
2. In VS Code open the Extensions view (`Ctrl+Shift+X`), click **⋯** (top-right) → **Install from VSIX…** and pick the file.

**Option B — build it yourself**
```bash
npm run install-theme
```
This packages the extension with [`vsce`](https://github.com/microsoft/vscode-vsce) and installs it into VS Code.

Then press `Ctrl+K` `Ctrl+T` (macOS: `Cmd+K` `Cmd+T`) and choose **Cave Dark Pro**.

> ⚠️ Copying the theme `.json` straight into `~/.vscode/extensions` (the old method) does **not** work — VS Code needs an extension manifest, which is why the theme is now a proper extension.

### 2. Install the font
Download [JetBrains Mono](https://www.jetbrains.com/lp/mono/), unzip, and install the files in `fonts/ttf`:
- **Windows:** select all → right-click → **Install for all users**
- **macOS:** double-click each file → **Install Font**
- **Linux:** copy to `~/.local/share/fonts` and run `fc-cache -f`

Restart VS Code afterwards.

### 3. Install the extensions

**macOS / Linux / Git Bash**
```bash
./scripts/install-extensions.sh          # everything
./scripts/install-extensions.sh --web    # web-development group only
```

**Windows PowerShell**
```powershell
.\scripts\install-extensions.ps1         # everything
.\scripts\install-extensions.ps1 -Web    # web-development group only
```
> If PowerShell blocks the script, run it once with:
> `powershell -ExecutionPolicy Bypass -File .\scripts\install-extensions.ps1`

Already-installed extensions are skipped, so it's safe to re-run. Only need some languages? Delete the groups you don't want from `extensions.json` first.

Opening this repo folder in VS Code will also show a **"Install recommended extensions"** prompt.

### 4. Apply the settings
1. `Ctrl+Shift+P` → **Preferences: Open User Settings (JSON)**
2. **Back up** what's there, then paste the contents of `settings.json` (or merge the parts you like).
3. Save. Settings take effect immediately.

### 5. Add the shortcuts *(optional)*
1. `Ctrl+Shift+P` → **Preferences: Open Keyboard Shortcuts (JSON)**
2. Paste the entries from `keybindings.json` **inside** the existing `[ ... ]` brackets.

### 6. Use the workspace template *(optional)*
Edit the folder paths in `workspace/cave.code-workspace` to point at your project, then **File → Open Workspace from File…**.

---

## ✂️ Snippets

Type the prefix and press `Tab`.

| Prefix | Language | Inserts |
|---|---|---|
| `html5` | HTML | Page boilerplate with meta, CSS and deferred JS |
| `flex-center` | CSS / SCSS | Flexbox centering |
| `grid-fit` | CSS / SCSS | Responsive auto-fit grid |
| `mq` | CSS / SCSS | Max-width media query |
| `sr-only` | CSS / SCSS | Screen-reader-only helper |
| `clg` / `clv` | JS / TS | `console.log` / labeled log |
| `afn` / `aafn` | JS / TS | Arrow / async arrow function |
| `fetchj` | JS / TS | `fetch` with status check + JSON |
| `tryc` | JS / TS | `try/catch` block |
| `rfc` | JSX / TSX | React function component (named after the file) |
| `ust` / `uef` | JSX / TSX | `useState` / `useEffect` |

## ⌨️ Shortcuts

| Action | Shortcut |
|---|---|
| Delete line | `Ctrl+Shift+K` |
| Duplicate line down / up | `Alt+Shift+↓` / `Alt+Shift+↑` |
| Toggle comment | `Ctrl+/` |
| Format document | `Shift+Alt+F` |
| Quick open file | `Ctrl+P` |
| Search in files | `Ctrl+Shift+F` |
| Toggle sidebar | `Ctrl+B` |
| Go to definition | `F12` |
| Toggle / new terminal | ``Ctrl+` `` / ``Ctrl+Shift+` `` |
| Start debugging / breakpoint | `F5` / `F9` |
| GitLens file blame | `Ctrl+Shift+G` then `Ctrl+B` |

On macOS, use `Cmd` in place of `Ctrl` and `Option` in place of `Alt`.

## 🧩 Extensions at a glance

- **Web:** Prettier, ESLint, Auto Close/Rename Tag, Path IntelliSense, Live Server, Tailwind CSS, ES7 React snippets, Pretty TS Errors, JS snippets
- **Java:** Java Extension Pack, Spring Boot Dev Pack
- **C / C++:** C/C++ Extension Pack, CMake Tools
- **C# / .NET:** C# Dev Kit, C#, DocComment
- **Python:** Python, Pylance, Debugpy, Jupyter, Black, Ruff
- **General:** GitLens, Copilot + Chat, Live Share, Docker, Thunder Client, Material Icons, Error Lens, Indent Rainbow, Todo Tree, Better Comments, Bookmarks, Color Highlight, Rainbow CSV

---

## ⚙️ Performance tips

- **Disable what you don't use.** Extensions → right-click → **Disable (Workspace)** keeps them off only for that project.
- **Find slow extensions.** `Ctrl+Shift+P` → **Developer: Show Running Extensions** shows activation time for each.
- **Heavy folders are excluded.** `node_modules`, `dist`, `build`, `coverage` and `.git` are left out of file watching and search.
- **Fewer open tabs.** The editor keeps at most 10 tabs per group and closes the oldest automatically.

## 💡 Five habits worth learning

1. **Command Palette** — `Ctrl+Shift+P` reaches every command without the mouse.
2. **Emmet** — type `ul>li*5` in HTML/JSX and press `Tab`.
3. **Multi-cursor** — `Alt`+click to add cursors, `Ctrl+D` to select the next match.
4. **Rename symbol** — `F2` renames a variable or function everywhere it's used.
5. **Zen Mode** — `Ctrl+K` then `Z` for distraction-free coding (`Esc` twice to exit).

---

## 🛠️ Troubleshooting

| Problem | Fix |
|---|---|
| **Cave Dark Pro** doesn't appear in the theme list | Install the `.vsix` (step 1), then **Developer: Reload Window**. |
| `code: command not found` | See the PATH note under **Quick start**. |
| Font looks unchanged | Install JetBrains Mono for all users and fully restart VS Code. |
| Formatter doesn't run on save | Install Prettier (and Black for Python), then check the file's language mode in the status bar. |
| Settings show yellow "unknown setting" warnings | The related extension isn't installed yet — run the installer script. |

## 📁 Project structure

```
vscode-theme/
├── package.json              # extension manifest (theme + snippets)
├── themes/cave-dark-pro-color-theme.json
├── snippets/                 # html, css, javascript, react
├── extensions.json           # curated extension list
├── scripts/                  # install-extensions.sh / .ps1
├── settings.json
├── keybindings.json
└── workspace/cave.code-workspace
```

## 🤝 Contributing

Issues and pull requests are welcome. To change the theme, edit `themes/cave-dark-pro-color-theme.json`, run `npm run install-theme`, then **Developer: Reload Window** to see the result. Please note changes in `CHANGELOG.md`.

## 👤 Author

**Shine** — founder of Cave Technologies
- GitHub: [@shineakhanda](https://github.com/shineakhanda)
- Email: [shineert35@gmail.com](mailto:shineert35@gmail.com)

## 📄 License

[MIT](LICENSE) © 2026 Shine · Cave Technologies
