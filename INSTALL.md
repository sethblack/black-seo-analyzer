# Installing Black SEO Analyzer

This document provides instructions for installing the Black SEO Analyzer tool on different operating systems.

If you'd rather watch than read, check out my YouTube videos:

[Windows Installation](https://youtu.be/WKq0-EHhuUw)

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

#### Windows MSI Installer

1. Download the latest Windows MSI installer (`setup.msi`) from the [releases page](https://github.com/sethblack/black-seo-analyzer/releases).
2. Run the `setup.msi` installer. This will install the application to `C:\Program Files (x86)\Black SEO Analyzer\` and add it to your system's PATH.
3. Open a new Command Prompt and verify the installation:

```cmd
black-seo-analyzer --version
```

### macOS (Basic) {#macos-basic}

1. Download the latest macOS binary from the [releases page](https://github.com/sethblack/black-seo-analyzer/releases).

2. Make the binary executable:

```bash
chmod +x <binary_name>
```

3. Move the binary to a location in your PATH:

```bash
sudo mv <binary_name> /usr/local/bin/black-seo-analyzer
```

4. Verify the installation:

```bash
black-seo-analyzer --version
```

### Linux (Basic) {#linux-basic}

1. Download the latest Linux binary for your architecture from the [releases page](https://github.com/sethblack/black-seo-analyzer/releases).

   - **x86_64**: For standard 64-bit Intel/AMD processors.
   - **arm**: For ARM-based processors, like those found in Raspberry Pi and some cloud servers.
   - **musl**: A version for containerized environments (e.g., Docker) that uses the musl C standard library.

2. Make the binary executable:

```bash
chmod +x <binary_name>
```

3. Move the binary to a location in your PATH:

```bash
sudo mv <binary_name> /usr/local/bin/black-seo-analyzer
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

1. Download the latest Windows executable file (`black-seo-analyzer.exe`) from the [releases page](https://github.com/sethblack/black-seo-analyzer/releases).

2. Move the downloaded `black-seo-analyzer.exe` to a directory that is included in your system's PATH, or add the directory containing the executable to your PATH.

3. To add the binary location to your PATH:
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
Usage: black-seo-analyzer.exe [OPTIONS] --url-to-begin-crawl <URL_TO_BEGIN_CRAWL>

Options:
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
          Optional argument to specify the output file
      --spa
          Optional flag to indicate if the site is a Single-Page Application (SPA)
      --is-sitemap
          Optional flag to indicate if the initial page is a sitemap.xml
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
      --anthropic-prompt-file <ANTHROPIC_PROMPT_FILE>
          Optional path to a file containing a custom Anthropic prompt
      --use-deepseek-analyzer
          Optional flag to enable DeepSeek API for SEO analysis
      --deepseek-api-key <DEEPSEEK_API_KEY>
          Optional DeepSeek API key (can also be set via DEEPSEEK_API_KEY environment variable)
      --deepseek-model <DEEPSEEK_MODEL>
          Optional DeepSeek model to use for analysis [default: deepseek-chat]
      --deepseek-prompt-file <DEEPSEEK_PROMPT_FILE>
          Optional path to a file containing a custom DeepSeek prompt
      --use-openai-analyzer
          Optional flag to enable OpenAI API for SEO analysis
      --openai-api-key <OPENAI_API_KEY>
          Optional OpenAI API key (can also be set via OPENAI_API_KEY environment variable)
      --openai-model <OPENAI_MODEL>
          Optional OpenAI model to use for analysis [default: gpt-4o]
      --openai-prompt-file <OPENAI_PROMPT_FILE>
          Optional path to a file containing a custom OpenAI prompt
      --use-gemini-analyzer
          Optional flag to enable Google Gemini API for SEO analysis
      --gemini-api-key <GEMINI_API_KEY>
          Optional Google Gemini API key (can also be set via GEMINI_API_KEY environment variable)
      --gemini-model <GEMINI_MODEL>
          Optional Google Gemini model to use for analysis [default: gemini-1.5-flash-latest]
      --gemini-prompt-file <GEMINI_PROMPT_FILE>
          Optional path to a file containing a custom Google Gemini prompt
      --user-agent <USER_AGENT>
          Optional User-Agent string for HTTP requests [default: "black-seo-analyzer v25.6.61905"]
      --max-pages <MAX_PAGES>
          Optional maximum number of pages to crawl
      --html-templates-dir <HTML_TEMPLATES_DIR>
          Optional path to custom HTML templates directory
      --headless
          Run in headless mode without launching the GUI [experimental] defaults to true
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

### Using Custom HTML Templates

You can provide your own HTML templates to customize the output appearance:

```bash
black-seo-analyzer --url-to-begin-crawl https://example.com --templates-dir ./my-templates
```

The templates directory should contain HTML template files with the same names as the default templates:
- base.html
- index_file.html
- page_file.html
- page.html
- preamble.html
- postamble.html

Any templates not found in the custom directory will fall back to the default templates.
