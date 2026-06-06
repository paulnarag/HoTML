HoTML macOS ARM64 Binary

HoTML is a CLI tool that generates HTML, CSS, and JavaScript boilerplate files.

INSTALLATION

1. Unzip hotml-macos-arm64.zip.

2. Before installing, open the hotml file first:
   - Right-click hotml
   - Choose Open
   - Wait until the help message appears
   - Close the window

3. Open Terminal in the unzipped folder.

4. Run:

   ./install.sh

After installation, use HoTML from anywhere:

   hotml help
   hotml create

Example:

   mkdir my-website
   cd my-website
   hotml create

HoTML will ask for filenames. Press Enter to use the defaults:

   index.html
   style.css
   script.js

TROUBLESHOOTING

If ./install.sh says permission denied, run:

   chmod +x install.sh
   ./install.sh