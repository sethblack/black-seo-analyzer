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

1. Download the latest Windows executable (`black-seo-analyzer.exe`) from the [releases page](https://github.com/sethblack/black-seo-analyzer/releases).

2. Move the downloaded `black-seo-analyzer.exe` file to a location of your choice (e.g., `C:\Program Files\black-seo-analyzer`).

3. Open Command Prompt and navigate to the directory where you placed the executable:

```cmd
cd C:\Program Files\black-seo-analyzer
```

4. Open Command Prompt and verify the installation:

```cmd
black-seo-analyzer.exe --version
```

5. Create a license.txt file in the same directory with your license key:

```cmd
echo "YOUR_LICENSE_KEY" > license.txt
```

#### Quick Start Example

Analyze a website and generate an HTML report:

```cmd
black-seo-analyzer.exe --url-to-begin-crawl https://example.com --output-type html-folder
```

### macOS (Basic) {#macos-basic}

1. Download the latest macOS binary (`black-seo-analyzer`) from the [releases page](https://github.com/sethblack/black-seo-analyzer/releases).

2. Move the downloaded binary to a location in your PATH (e.g., `/usr/local/bin/`):

```bash
sudo mv /path/to/downloaded/black-seo-analyzer /usr/local/bin/
```
   *(Replace `/path/to/downloaded/black-seo-analyzer` with the actual path to the downloaded file)*

3. Make it executable:

```bash
sudo chmod +x /usr/local/bin/black-seo-analyzer
```

4. Verify the installation:

```bash
black-seo-analyzer --version
```

5. Create a license.txt file in the same directory as the binary (`/usr/local/bin/` in this example) or your working directory with your license key:

```bash
echo "YOUR_LICENSE_KEY" > license.txt
```

#### Quick Start Example

Analyze a website and generate an HTML report:

```bash
black-seo-analyzer --url-to-begin-crawl https://example.com --output-type html-folder
```

### Linux (Basic) {#linux-basic}

#### Ubuntu/Debian

1. Download the latest Linux binary (`black-seo-analyzer`) for your architecture from the [releases page](https://github.com/sethblack/black-seo-analyzer/releases).

2. Move the downloaded binary to a location in your PATH (e.g., `/usr/local/bin/`):

```bash
sudo mv /path/to/downloaded/black-seo-analyzer /usr/local/bin/
```
   *(Replace `/path/to/downloaded/black-seo-analyzer` with the actual path to the downloaded file)*

3. Make it executable:

```bash
sudo chmod +x /usr/local/bin/black-seo-analyzer
```

4. Verify the installation:

```bash
black-seo-analyzer --version
```

#### Fedora/RHEL/CentOS

1. Download the latest Linux binary (`black-seo-analyzer`) for your architecture from the [releases page](https://github.com/sethblack/black-seo-analyzer/releases).

2. Move the downloaded binary to a location in your PATH (e.g., `/usr/local/bin/`):

```bash
sudo mv /path/to/downloaded/black-seo-analyzer /usr/local/bin/
```
   *(Replace `/path/to/downloaded/black-seo-analyzer` with the actual path to the downloaded file)*

3. Make it executable:

```bash
sudo chmod +x /usr/local/bin/black-seo-analyzer
```

4. Verify the installation:

```bash
black-seo-analyzer --version
```

#### Quick Start Example

Analyze a website and generate an HTML report:

```bash
black-seo-analyzer --url-to-begin-crawl https://example.com --output-type html-folder
```

## Advanced Installation

### Windows (Advanced) {#windows-advanced}


#### Manual Installation

1. Download the latest Windows executable (`black-seo-analyzer.exe`) from the [releases page](https://github.com/sethblack/black-seo-analyzer/releases).

2. Place the downloaded `black-seo-analyzer.exe` file in a location of your choice (e.g., `C:\Program Files\black-seo-analyzer`).

3. Add the directory containing the executable to your system's PATH environment variable:
   - Right-click on "This PC" or "My Computer" and select "Properties"
   - Click on "Advanced system settings"
   - Click on "Environment Variables"
   - Under "System variables", find and select "Path", then click "Edit"
   - Click "New" and add the path to the directory containing the executable (e.g., `C:\Program Files\black-seo-analyzer`)
   - Click "OK" on all dialogs to save the changes

4. Open a *new* Command Prompt (existing ones won't see the updated PATH) and verify the installation:

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
      --url-to-begin-crawl <URL_TO_BEGIN_CRAWL>
          URL of the sitemap to analyze
      --log-file <LOG_FILE>
          Path to log file
      --output-type <OUTPUT_TYPE>
          Output format type [default: html-folder] [possible values: json, jsonl, xml, csv, csv-flat, html-folder, json-files]
      --concurrent-requests <CONCURRENT_REQUESTS>
          Optional Number of concurrent requests to make [default: 20]
      --rate-limit <RATE_LIMIT>
          Optional Rate limit in milliseconds [default: 50]
      --output-file <OUTPUT_FILE>

      --spa

      --is-sitemap

      --disable-external-links
          Optional flag to disable external link checking
      --locale <LOCALE>
          Optional locale for internationalization [default: en]
      --use-anthropic-analyzer
          Optional flag to enable Anthropic Claude API for SEO analysis
      --anthropic-api-key <ANTHROPIC_API_KEY>
          Optional Anthropic API key (can also be set via ANTHROPIC_API_KEY environment variable)
      --anthropic-model <ANTHROPIC_MODEL>
          Optional Anthropic model to use for analysis [default: claude-3-haiku-20240307]
      --user-agent <USER_AGENT>
          Optional User-Agent string for HTTP requests [default: "black-seo-analyzer v2025.1.10000"]
      --max-pages <MAX_PAGES>
          Optional maximum number of pages to crawl
  -h, --help
          Print help
  -V, --version
          Print version
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
black-seo-analyzer --url-to-begin-crawl https://example.com --output-type json --output-file report.json

# CSV output
black-seo-analyzer --url-to-begin-crawl https://example.com --output-type csv --output-file report.csv

# XML output
black-seo-analyzer --url-to-begin-crawl https://example.com --output-type xml --output-file report.xml
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
