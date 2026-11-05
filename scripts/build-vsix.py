"""Package the extension into a .vsix without needing npm/vsce.

Usage:
  python scripts/build-vsix.py               # theme + icons + snippets
  python scripts/build-vsix.py --theme-only  # theme + icons, no snippets
"""
import json, os, sys, zipfile
from xml.sax.saxutils import escape

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(root)
theme_only = "--theme-only" in sys.argv

pkg = json.load(open("package.json"))
pkg.pop("scripts", None)
if theme_only:
    pkg["contributes"].pop("snippets", None)
    pkg["categories"] = ["Themes"]

files = ["README.md", "CHANGELOG.md", "LICENSE", "themes/cave-dark-pro-color-theme.json", "themes/cave-icons.json"]
files += ["icons/" + f for f in sorted(os.listdir("icons"))]
if not theme_only:
    files += ["snippets/" + f for f in sorted(os.listdir("snippets"))]

rename = {"README.md": "readme.md", "CHANGELOG.md": "changelog.md", "LICENSE": "LICENSE.txt"}
manifest = f"""<?xml version="1.0" encoding="utf-8"?>
<PackageManifest Version="2.0.0" xmlns="http://schemas.microsoft.com/developer/vsx-schema/2011" xmlns:d="http://schemas.microsoft.com/developer/vsx-schema-design/2011">
  <Metadata>
    <Identity Language="en-US" Id="{pkg['name']}" Version="{pkg['version']}" Publisher="{pkg['publisher']}" />
    <DisplayName>{escape(pkg['displayName'])}</DisplayName>
    <Description xml:space="preserve">{escape(pkg['description'])}</Description>
    <Tags>{escape(','.join(pkg.get('keywords', [])))}</Tags>
    <Categories>{','.join(pkg['categories'])}</Categories>
    <GalleryFlags>Public</GalleryFlags>
    <Properties>
      <Property Id="Microsoft.VisualStudio.Code.Engine" Value="{pkg['engines']['vscode']}" />
      <Property Id="Microsoft.VisualStudio.Code.ExtensionKind" Value="ui,workspace" />
      <Property Id="Microsoft.VisualStudio.Services.Links.Source" Value="{pkg['repository']['url']}" />
      <Property Id="Microsoft.VisualStudio.Services.Branding.Color" Value="#15161e" />
      <Property Id="Microsoft.VisualStudio.Services.Branding.Theme" Value="dark" />
    </Properties>
    <License>extension/LICENSE.txt</License>
  </Metadata>
  <Installation><InstallationTarget Id="Microsoft.VisualStudio.Code"/></Installation>
  <Dependencies/>
  <Assets>
    <Asset Type="Microsoft.VisualStudio.Code.Manifest" Path="extension/package.json" Addressable="true" />
    <Asset Type="Microsoft.VisualStudio.Services.Content.Details" Path="extension/readme.md" Addressable="true" />
    <Asset Type="Microsoft.VisualStudio.Services.Content.Changelog" Path="extension/changelog.md" Addressable="true" />
    <Asset Type="Microsoft.VisualStudio.Services.Content.License" Path="extension/LICENSE.txt" Addressable="true" />
  </Assets>
</PackageManifest>"""
types = ('<?xml version="1.0" encoding="utf-8"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
         '<Default Extension=".json" ContentType="application/json"/><Default Extension=".md" ContentType="text/markdown"/>'
         '<Default Extension=".txt" ContentType="text/plain"/><Default Extension=".svg" ContentType="image/svg+xml"/>'
         '<Default Extension=".vsixmanifest" ContentType="text/xml"/></Types>')

out = f"{pkg['name']}{'-theme-only' if theme_only else ''}-{pkg['version']}.vsix"
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    z.writestr("[Content_Types].xml", types)
    z.writestr("extension.vsixmanifest", manifest)
    z.writestr("extension/package.json", json.dumps(pkg, indent=2))
    for f in files:
        z.write(f, "extension/" + rename.get(f, f))
print("Built", out)
