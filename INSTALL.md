# Installing Black SEO Analyzer

This document provides instructions for installing the Black SEO Analyzer tool on different operating systems.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Basic Installation](#basic-installation)
  - [Windows](#windows-basic)
  - [macOS](#macos-basic)
  - [Linux](#linux-basic)
- [Advanced Installation](#advanced-installation)
  - [Windows](#windows-advanced)
- [Verifying Installation](#verifying-installation)
- [Troubleshooting](#troubleshooting)

## Prerequisites

Before installing Black SEO Analyzer, ensure you have the following:

- Internet connection for downloading the tool
- Basic familiarity with command-line interfaces (for basic installation)
- Administrator/sudo privileges (may be required for some installation methods)

## Basic Installation

### Windows (Basic) {#windows-basic}

1. Download the latest Windows zip file (.zip) from the [releases page](https://github.com/sethblack/black-seo-analyzer/releases).

2. Right-click and extract the ZIP file to a location of your choice (e.g., `C:\Program Files\black-seo-analyzer`).

3. Open Command Prompt as Administrator and navigate to the extracted directory:

```cmd
cd C:\Program Files\black-seo-analyzer
```

4. Open Command Prompt and verify the installation:

```cmd
black-seo-analyzer --version
```

5. Create a license.txt file in the same directory with your license key:

```cmd
echo "YOUR_LICENSE_KEY" > license.txt
```

#### Quick Start Example

Analyze a website and generate an HTML report:

```cmd
black-seo-analyzer --url-to-begin-crawl https://example.com --output-type HtmlFolder
```

### macOS (Basic) {#macos-basic}

1. Download the latest macOS binary (.tar.gz) from the [releases page](https://github.com/sethblack/black-seo-analyzer/releases).

2. Extract the archive:

```bash
tar -xzf black-seo-analyzer-macos.tar.gz
```

3. Move the binary to a location in your PATH:

```bash
sudo mv black-seo-analyzer /usr/local/bin/
```

4. Make it executable:

```bash
sudo chmod +x /usr/local/bin/black-seo-analyzer
```

5. Verify the installation:

```bash
black-seo-analyzer --version
```

6. Create a license.txt file in the same directory with your license key:

```bash
echo "YOUR_LICENSE_KEY" > license.txt
```

#### Quick Start Example

Analyze a website and generate an HTML report:

```bash
black-seo-analyzer --url-to-begin-crawl https://example.com --output-type HtmlFolder
```

### Linux (Basic) {#linux-basic}

#### Ubuntu/Debian

1. Download the latest Linux binary (.tar.gz) for your architecture from the [releases page](https://github.com/sethblack/black-seo-analyzer/releases).

2. Extract the archive:

```bash
tar -xzf black-seo-analyzer-linux-x86_64.tar.gz
```

3. Move the binary to a location in your PATH:

```bash
sudo mv black-seo-analyzer /usr/local/bin/
```

4. Make it executable:

```bash
sudo chmod +x /usr/local/bin/black-seo-analyzer
```

5. Verify the installation:

```bash
black-seo-analyzer --version
```

#### Fedora/RHEL/CentOS

1. Download the latest Linux binary (.tar.gz) for your architecture from the [releases page](https://github.com/sethblack/black-seo-analyzer/releases).

2. Extract the archive:

```bash
tar -xzf black-seo-analyzer-linux-x86_64.tar.gz
```

3. Move the binary to a location in your PATH:

```bash
sudo mv black-seo-analyzer /usr/local/bin/
```

4. Make it executable:

```bash
sudo chmod +x /usr/local/bin/black-seo-analyzer
```

5. Verify the installation:

```bash
black-seo-analyzer --version
```

#### Quick Start Example

Analyze a website and generate an HTML report:

```bash
black-seo-analyzer --url-to-begin-crawl https://example.com --output-type HtmlFolder
```

## Advanced Installation

### Windows (Advanced) {#windows-advanced}


#### Manual Installation

1. Download the latest Windows binary (.zip) from the [releases page](https://github.com/sethblack/black-seo-analyzer/releases).

2. Extract the ZIP file to a location of your choice (e.g., `C:\Program Files\black-seo-analyzer`).

3. Add the binary location to your PATH:
   - Right-click on "This PC" or "My Computer" and select "Properties"
   - Click on "Advanced system settings"
   - Click on "Environment Variables"
   - Under "System variables", find and select "Path", then click "Edit"
   - Click "New" and add the path to the directory containing the binary (e.g., `C:\Program Files\black-seo-analyzer`)
   - Click "OK" on all dialogs to save the changes

4. Open a new Command Prompt and verify the installation:

```cmd
black-seo-analyzer --version
```


## Verifying Installation

After installation, verify that Black SEO Analyzer is working correctly:

```bash
black-seo-analyzer --version
```

You should see output similar to:

```
black-seo-analyzer 2025.1.6
```

## Troubleshooting

### Common Issues

#### "Command not found" error

- Ensure the installation directory is in your PATH
- Try restarting your terminal or command prompt

#### Missing dependencies

If you encounter errors about missing dependencies:

- Windows: Install the [Visual C++ Redistributable](https://aka.ms/vs/17/release/vc_redist.x64.exe)
- Linux: Install required libraries:
  ```bash
  # Ubuntu/Debian
  sudo apt-get install libssl-dev pkg-config
  
  # Fedora/RHEL/CentOS
  sudo dnf install openssl-devel pkgconfig
  ```
- macOS: Install required libraries:
  ```bash
  brew install openssl@3
  ```

#### Permission denied

If you get "permission denied" errors when running the tool:

- Windows: Run Command Prompt as Administrator
- macOS/Linux: Use sudo or ensure the binary has execute permissions:
  ```bash
  sudo chmod +x /path/to/black-seo-analyzer
  ```

### Getting Help

If you encounter issues not covered in this guide:

1. Check the [GitHub Issues](https://github.com/sethblack/black-seo-analyzer/issues) for similar problems and solutions
2. Open a new issue with details about your problem
3. Contact support at support@example.com

## Command-Line Options

Black SEO Analyzer supports various command-line options:

```
USAGE:
    black-seo-analyzer [OPTIONS] --url-to-begin-crawl <URL>

OPTIONS:
    --url-to-begin-crawl <URL>       URL of the website to analyze
    --log-file <FILE>                Path to log file (optional)
    --output-type <TYPE>             Output format type [default: HtmlFolder]
                                     [possible values: Json, Jsonl, Xml, Csv, CsvFlat, HtmlFolder]
    --concurrent-requests <NUM>      Number of concurrent requests [default: 20]
    --rate-limit <MS>                Rate limit in milliseconds [default: 50]
    --output-file <FILE>             Output file path (optional)
    --spa                            Enable SPA mode for single-page applications
    --is-sitemap                     Treat the URL as a sitemap
    --locale <LOCALE>                Locale for internationalization [default: en]
    -h, --help                       Print help information
    -V, --version                    Print version information
```

## Examples

### Basic Website Analysis

```bash
black-seo-analyzer --url-to-begin-crawl https://example.com
```

### Analyzing a Single-Page Application (SPA)

```bash
black-seo-analyzer --url-to-begin-crawl https://example.com --spa
```

### Analyzing a Sitemap

```bash
black-seo-analyzer --url-to-begin-crawl https://example.com/sitemap.xml --is-sitemap
```

### Generating Different Output Formats

```bash
# JSON output
black-seo-analyzer --url-to-begin-crawl https://example.com --output-type Json --output-file report.json

# CSV output
black-seo-analyzer --url-to-begin-crawl https://example.com --output-type Csv --output-file report.csv

# XML output
black-seo-analyzer --url-to-begin-crawl https://example.com --output-type Xml --output-file report.xml
```

### Adjusting Crawl Settings

```bash
# Increase concurrent requests for faster crawling
black-seo-analyzer --url-to-begin-crawl https://example.com --concurrent-requests 30

# Increase rate limit for slower crawling (more gentle on the server)
black-seo-analyzer --url-to-begin-crawl https://example.com --rate-limit 100
```

### Using a Different Language

```bash
black-seo-analyzer --url-to-begin-crawl https://example.com --locale es
```
