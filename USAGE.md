# SEO Analyzer Usage

This document provides detailed information on how to use the command-line interface (CLI) for the SEO Analyzer.

## Table of Contents

- [Basic Usage](#basic-usage)
- [General Arguments](#general-arguments)
- [Output Configuration](#output-configuration)
- [Crawler Configuration](#crawler-configuration)
- [AI-Powered Analysis](#ai-powered-analysis)
  - [Anthropic Claude](#anthropic-claude)
  - [DeepSeek](#deepseek)
  - [OpenAI](#openai)
  - [Google Gemini](#google-gemini)
- [Advanced Configuration](#advanced-configuration)

---

## Basic Usage

To run the SEO Analyzer, you need to provide a starting URL. The tool will then crawl the website and generate a report.

**Interactive Mode (if no URL is provided):**

If you run the application without the `--url-to-begin-crawl` argument, it will prompt you to enter a URL.

```bash
seo-analyzer
```

**Expected Output:**
```
Please enter the URL to begin the crawl: [type your URL here and press Enter]
```

**Direct URL:**

You can provide the URL directly using the `--url-to-begin-crawl` argument.

```bash
seo-analyzer --url-to-begin-crawl "https://www.example.com"
```

**Expected Output:**
The analyzer will start crawling from the specified URL and, by default, create an HTML report in a folder named after the domain (e.g., `example-com_YYYYMMDDHHMMSS`).

---

## General Arguments

### `--url-to-begin-crawl`

Specifies the starting URL for the crawl. This can be a homepage, a sitemap, or any other page on the site.

- **Type:** `String`
- **Required:** Yes (unless running in interactive mode)

**Example:**
```bash
seo-analyzer --url-to-begin-crawl "https://www.sethserver.com"
```

### `--log-file`

Redirects logging output to a specified file instead of the console.

- **Type:** `String`
- **Optional**

**Example:**
```bash
seo-analyzer --url-to-begin-crawl "https://www.example.com" --log-file "crawl.log"
```
**Expected Behavior:**
A file named `crawl.log` will be created in the current directory containing all the log messages from the crawl. If not specified, logs will be printed to the console.

### `--locale`

Sets the language for the generated report and log messages.

- **Type:** `String`
- **Default:** `en`
- **Available:** `en`, `es`, `zh-CN` (and others if translation files are added)

**Example (Spanish):**
```bash
seo-analyzer --url-to-begin-crawl "https://www.example.com" --locale "es"
```

---

## Output Configuration

### `--output-type`

Defines the format of the analysis report.

- **Type:** `Enum`
- **Default:** `html-folder`
- **Values:**
  - `html-folder`: Creates a directory with an `index.html` file and separate HTML files for each crawled page. The template can be customized with `--html-templates-dir`.
  - `json`: A single JSON file containing all results.
  - `jsonl`: A JSONL file where each line is a JSON object for a crawled page.
  - `xml`: A single XML file with all results.
  - `csv`: A CSV file with results.
  - `csv-flat`: A flattened CSV file.
  - `json-files`: Creates a directory with individual JSON files for each crawled page.

**Example (JSONL):**
```bash
seo-analyzer --url-to-begin-crawl "https://www.example.com" --output-type "jsonl"
```
**Expected Output:**
A file named `example-com_YYYYMMDDHHMMSS.jsonl` will be created.

### `--output-file`

Specifies a custom name for the output file or directory.

- **Type:** `String`
- **Optional**

**Example (Custom HTML folder name):**
```bash
seo-analyzer --url-to-begin-crawl "https://www.example.com" --output-type "html-folder" --output-file "my-seo-report"
```
**Expected Output:**
A directory named `my-seo-report` will be created containing the HTML report.

**Example (Custom JSON file name):**
```bash
seo-analyzer --url-to-begin-crawl "https://www.example.com" --output-type "json" --output-file "report.json"
```
**Expected Output:**
A file named `report.json` will be created.

### `--html-templates-dir`

Specifies a path to a directory containing custom HTML templates for the report. This allows you to customize the look and feel of the `html-folder` output.

- **Type:** `String`
- **Optional**

**Example:**
```bash
seo-analyzer --url-to-begin-crawl "https://www.example.com" --html-templates-dir "./my-custom-templates"
```

The templates directory should contain HTML template files with the same names as the default templates:
- base.html
- index_file.html
- page_file.html
- page.html
- preamble.html
- postamble.html

Any templates not found in the custom directory will fall back to the default templates.

---

## Crawler Configuration

### `--concurrent-requests`

Sets the number of concurrent requests the crawler can make.

- **Type:** `Integer`
- **Default:** `20`

**Example:**
```bash
seo-analyzer --url-to-begin-crawl "https://www.example.com" --concurrent-requests 10
```

### `--rate-limit`

Sets the delay in milliseconds between requests to avoid overloading the server.

- **Type:** `Integer` (milliseconds)
- **Default:** `50`

**Example:**
```bash
seo-analyzer --url-to-begin-crawl "https://www.example.com" --rate-limit 100
```

### `--spa`

Indicates that the target website is a Single-Page Application (SPA). This enables a browser-based crawler to render JavaScript.

- **Type:** `Boolean`
- **Default:** `false`

**Example:**
```bash
seo-analyzer --url-to-begin-crawl "https://my-react-app.com" --spa
```

### `--is-sitemap`

Indicates that the initial URL is a `sitemap.xml` file. The crawler will parse the sitemap and crawl the URLs listed within it.

- **Type:** `Boolean`
- **Default:** `false`

**Example:**
```bash
seo-analyzer --url-to-begin-crawl "https://www.example.com/sitemap.xml" --is-sitemap
```

### `--disable-external-links`

Prevents the crawler from checking the status of external links found on the pages.

- **Type:** `Boolean`
- **Default:** `false`

**Example:**
```bash
seo-analyzer --url-to-begin-crawl "https://www.example.com" --disable-external-links
```

### `--user-agent`

Sets a custom User-Agent string for all HTTP requests made by the crawler. This is useful for identifying your crawler in server logs or when you need to exclude it from your Analytics.

- **Type:** `String`
- **Default:** `black-seo-analyzer v[VERSION]`

**Example:**
```bash
seo-analyzer --url-to-begin-crawl "https://www.example.com" --user-agent "MyCustomCrawler/1.0"
```

### `--max-pages`

Sets the maximum number of pages to crawl. This is useful for large websites or for quick scans. Note that the effective limit may also be constrained by your license tier.

- **Type:** `Integer`
- **Optional**

**Example:**
```bash
seo-analyzer --url-to-begin-crawl "https://www.large-website.com" --max-pages 50
```

---

## AI-Powered Analysis

You can enhance the SEO analysis with AI models from various providers. This requires enabling the specific provider and providing an API key.

### Anthropic Claude

- **`--use-anthropic-analyzer`**: Enables analysis using the Anthropic Claude API.
- **`--anthropic-api-key`**: Your Anthropic API key. Can also be set via the `ANTHROPIC_API_KEY` environment variable.
- **`--anthropic-model`**: The model to use. (Default: `claude-3-haiku-20240307`)
- **`--anthropic-prompt-file`**: Path to a file with a custom prompt.

**Example:**
```bash
seo-analyzer --url-to-begin-crawl "https://www.example.com" \
  --use-anthropic-analyzer \
  --anthropic-api-key "YOUR_ANTHROPIC_API_KEY"
```

### DeepSeek

- **`--use-deepseek-analyzer`**: Enables analysis using the DeepSeek API.
- **`--deepseek-api-key`**: Your DeepSeek API key. Can also be set via the `DEEPSEEK_API_KEY` environment variable.
- **`--deepseek-model`**: The model to use. (Default: `deepseek-chat`)
- **`--deepseek-prompt-file`**: Path to a file with a custom prompt.

**Example:**
```bash
seo-analyzer --url-to-begin-crawl "https://www.example.com" \
  --use-deepseek-analyzer \
  --deepseek-api-key "YOUR_DEEPSEEK_API_KEY"
```

### OpenAI

- **`--use-openai-analyzer`**: Enables analysis using the OpenAI API.
- **`--openai-api-key`**: Your OpenAI API key. Can also be set via the `OPENAI_API_KEY` environment variable.
- **`--openai-model`**: The model to use. (Default: `gpt-4o`)
- **`--openai-prompt-file`**: Path to a file with a custom prompt.

**Example:**
```bash
seo-analyzer --url-to-begin-crawl "https://www.example.com" \
  --use-openai-analyzer \
  --openai-api-key "YOUR_OPENAI_API_KEY"
```

### Google Gemini

- **`--use-gemini-analyzer`**: Enables analysis using the Google Gemini API.
- **`--gemini-api-key`**: Your Gemini API key. Can also be set via the `GEMINI_API_KEY` environment variable.
- **`--gemini-model`**: The model to use. (Default: `gemini-1.5-flash-latest`)
- **`--gemini-prompt-file`**: Path to a file with a custom prompt.

**Example:**
```bash
seo-analyzer --url-to-begin-crawl "https://www.example.com" \
  --use-gemini-analyzer \
  --gemini-api-key "YOUR_GEMINI_API_KEY"
```
