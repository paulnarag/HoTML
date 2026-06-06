
# HoTML

HoTML is a CLI tool that generates HTML, CSS, and JavaScript boilerplate files.

It is called HoTML because boiling is hot, and this tool creates boilerplate files for HTML, CSS, and JavaScript.

## Download

Download the latest macOS ARM64 binary from the GitHub Releases page:

```text
hotml-macos-arm64.zip
```

## Installation

Unzip the file.

Before running the installer, open the `hotml` file first:

1. Right-click `hotml`
2. Choose **Open**
3. Wait until the help message appears
4. Close the window

Then open Terminal in the unzipped folder and run:

```bash
./install.sh
```

After installation, HoTML can be used globally from anywhere:

```bash
hotml help
hotml create
```

## Usage

Create a new project folder:

```bash
mkdir my-website
cd my-website
hotml create
```

HoTML will ask for filenames:

```text
HTML file (index.html):
CSS file (style.css):
JS file (script.js):
```

Press Enter to use the default names, or type custom filenames.

## Troubleshooting

If `./install.sh` says permission denied, run:

```bash
chmod +x install.sh
./install.sh
```

If `hotml` is still not found after installation, restart Terminal and try again:

```bash
hotml help
```
