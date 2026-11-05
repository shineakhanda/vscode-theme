# Installs every extension listed in extensions.json (Windows PowerShell).
# Usage:  .\scripts\install-extensions.ps1          install all
#         .\scripts\install-extensions.ps1 -Web     web-development group only
param([switch]$Web)
$ErrorActionPreference = "Stop"
Set-Location (Join-Path $PSScriptRoot "..")

if (-not (Get-Command code -ErrorAction SilentlyContinue)) {
  Write-Host "X 'code' command not found. Reinstall VS Code with 'Add to PATH' checked, then reopen PowerShell." -ForegroundColor Red
  exit 1
}

$text = Get-Content extensions.json -Raw
if ($Web) { $text = ($text -split 'Java')[0] }
$clean = ($text -split "`n" | ForEach-Object { ($_ -replace '//.*$', '') }) -join "`n"
$ids = [regex]::Matches($clean, '"([A-Za-z0-9-]+\.[A-Za-z0-9.-]+)"') | ForEach-Object { $_.Groups[1].Value }

$installed = (code --list-extensions) | ForEach-Object { $_.ToLower() }
foreach ($id in $ids) {
  if ($installed -contains $id.ToLower()) {
    Write-Host "OK $id (already installed)" -ForegroundColor Green
  } else {
    Write-Host "-> installing $id"
    code --install-extension $id --force | Out-Null
  }
}
Write-Host "Done."
