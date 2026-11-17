# Black SEO Analyzer

A powerful tool for comprehensive SEO analysis, designed for SEO professionals and developers who want to ensure their websites are optimized for both search engines and AI systems.

When run without a license you're limited in the number of pages you can crawl, but no other functionality is restricted. To purchase a license and unlock unlimited analysis power, visit [Black SEO Analyzer product page](https://www.blackseoanalyzer.com/).

![Black SEO Analyzer](https://www.sethserver.com/static/images/black-seo-analyzer.png)

## MCP server: technical SEO audits inside your AI assistant

Black SEO Analyzer is also a [Model Context Protocol](https://modelcontextprotocol.io/) (MCP) server, published in the official MCP registry as `io.github.sethblack/bseoa`. It gives Claude, ChatGPT, Cursor, VS Code, Codex and other MCP hosts a technical SEO crawler they can call as tools: check one page, crawl a whole site, rank the issues, and compare two crawls. Crawl results are stored, so they are still there in the next chat.

### Hosted connector (nothing to install)

```
https://mcp.blackseoanalyzer.com/mcp
```

Streamable HTTP with OAuth sign-in. Add the URL as a connector in Claude or ChatGPT, or in any other assistant that takes a remote MCP URL with sign-in. Crawls run on our servers and the results are kept for your account. The first 14 days are free, with no card; plans are on the [pricing page](https://www.blackseoanalyzer.com/pricing). JavaScript rendering is not available on the hosted connector; the desktop app and the CLI have it.

### Local server (stdio)

The `bseoa` binary runs the same server on your own machine with `bseoa mcp`.

1. Install it with `brew install sethblack/bseoa/bseoa` (macOS and Linux), or download `bseoa` for your OS from the [releases page](https://github.com/sethblack/black-seo-analyzer/releases) and put it on your `PATH`. The Linux binary needs glibc 2.39 or newer (Ubuntu 24.04, Debian 13 or later).
2. Start a [free 14-day trial](https://www.blackseoanalyzer.com/free-trial) and store the key once with `bseoa license store <your-license-key>`. Without a key every tool returns a license error.
3. Add the server to your host:

| Host | Setup |
| --- | --- |
| Claude Desktop | Download the `.mcpb` bundle for your OS from the [releases page](https://github.com/sethblack/black-seo-analyzer/releases) and double-click it. It carries its own copy of the binary. |
| Claude Code | `claude mcp add bseoa -s user -- bseoa mcp` |
| Codex CLI | `codex mcp add bseoa -- bseoa mcp` |
| Gemini CLI | `gemini mcp add bseoa bseoa mcp` |
| Cursor | Add the JSON below to `~/.cursor/mcp.json` |

```json
{
  "mcpServers": {
    "bseoa": {
      "command": "bseoa",
      "args": ["mcp"]
    }
  }
}
```

Setup for every host, with prompts to try, is on the [connector page](https://www.blackseoanalyzer.com/mcp).

### Tools

| Tool | What it does |
| --- | --- |
| `check_page` | Audit one URL immediately and return its SEO issues. |
| `start_crawl` | Start crawling a whole site in the background and return a job id. |
| `crawl_status` | Report the progress and state of a background crawl. |
| `list_crawls` | List the stored crawls with their start URL, dates and page count. |
| `issues_summary` | Summarize a crawl: counts by severity, category and issue key, with example URLs. |
| `query_issues` | List individual issues from a crawl, filtered by severity, key, category or URL prefix. |
| `page_report` | Report everything recorded about one crawled URL, including its full issue list. |
| `compare_crawls` | Compare two crawls and report new, fixed and persisting issues. |
| `serp_preview` | Show how each URL's title and description will look in a search result, including truncation. |
| `search_docs` | Search bseoa's own documentation: tools, flags, limits, licenses and issue keys. |
| `account_status` | Hosted connector only. Report your plan, the pages used and left, and how long results are kept. |

No tool returns page HTML. Issues use a stable schema (`bseoa.issue/v1`) with a key, a category, a severity, the affected URL, a message and a fix hint.

## Overview

Black SEO Analyzer is a powerful tool that keeps your website visible in both traditional search results and AI-generated responses. Good technical SEO isn't just about Google rankings—it's about making sure AI systems can find and understand your content when people ask about you.

When your site's structure and metadata are optimized correctly, you'll appear in both search results and AI conversations. Black SEO Analyzer cuts through the noise and tells you exactly what's holding your site back - without corporate buzzwords, just actionable data so you don't get left behind when someone asks an AI about exactly what you sell.

## True Ownership, Not Subscription

Unlike subscription-based tools that stop working when you stop paying, Black SEO Analyzer offers genuine software ownership. Your purchase includes a legally-binding source code access guarantee if we ever discontinue the product — protecting your investment permanently.

**Black SEO Analyzer License: One-Time Purchase**
- Lifetime software ownership
- All future updates
- Command-line efficiency
- Source code escrow guarantee
- Unlimited URLs and sites
- All advanced features included

## Installation

Please read the [INSTALL.md](INSTALL.md) file for installation instructions.

## Windows Usage

```
A comprehensive SEO analysis tool

Usage: black-seo-analyzer.exe [OPTIONS]

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
          Directory holding replacements for the built-in HTML report templates
  -h, --help
          Print help
  -V, --version
          Print version
```

### Windows Example Usage

#### Basic JSON output for one site
```bash
black-seo-analyzer.exe --url-to-begin-crawl https://example.com --output-type json --output-file example-report.json
```

#### Website with a sitemap
```bash
black-seo-analyzer.exe --url-to-begin-crawl https://example.com/sitemap.xml --is-sitemap --output-type json --output-file sitemap-report.json
```

#### Single page app
```bash
black-seo-analyzer.exe --url-to-begin-crawl https://spa-example.com --spa --output-type json --output-file spa-report.json
```

#### HTML folder output
```bash
black-seo-analyzer.exe --url-to-begin-crawl https://example.com --output-type html-folder --output-file ./seo-reports
```

## Linux/MacOS Usage

```
A comprehensive SEO analysis tool

Usage: black-seo-analyzer [OPTIONS]

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
          Optional User-Agent string for HTTP requests [default: "black-seo-analyzer v2025.1.100001"]
      --max-pages <MAX_PAGES>
          Optional maximum number of pages to crawl
      --html-templates-dir <HTML_TEMPLATES_DIR>
          Directory holding replacements for the built-in HTML report templates
  -h, --help
          Print help
  -V, --version
          Print version
```

### Linux/MacOS Example Usage

Notes:

* If the binary is not executable, you may need to run `chmod +x ./black-seo-analyzer` first.
* The examples below assume the binary is in the current directory. If it's in a different directory, you'll need to provide the full path to the binary or if it is in your PATH, you can just run `black-seo-analyzer`.

#### Basic JSON output for one site
```bash
./black-seo-analyzer --url-to-begin-crawl https://example.com --output-type json --output-file example-report.json
```

#### Website with a sitemap
```bash
./black-seo-analyzer.exe --url-to-begin-crawl https://example.com/sitemap.xml --is-sitemap --output-type json --output-file sitemap-report.json
```

#### Single page app
```bash
./black-seo-analyzer.exe --url-to-begin-crawl https://spa-example.com --spa --output-type json --output-file spa-report.json
```

#### HTML folder output
```bash
./black-seo-analyzer.exe --url-to-begin-crawl https://example.com --output-type html-folder --output-file ./seo-reports
```

## Comprehensive Feature List

### Core Functionality
- Command-line interface
- GUI interface
- Crawl websites starting from a specified URL
- Crawl websites using a sitemap
- Support for both static websites (HTTP requests) and Single Page Applications (SPAs) via headless browser
- Configurable concurrent request limit
- Configurable maximum page limit
- Detailed logging system
- Configurable log file location

### Crawling Capabilities
- HTTP request-based crawler
- Headless browser-based crawler
- Automatic detection and extraction of links, scripts, stylesheets, images
- Sitemap parsing and processing
- Asynchronous processing for crawling and analysis
- Content hash generation (SHA1) for duplicate content detection
- Configurable crawl delay
- Respect robots.txt
- User-agent customization
- Domain extraction utility

### SEO Analysis Modules
- **Content Analysis**
    - Word count
    - Keyword density analysis
    - Readability analysis (Flesch-Kincaid score, syllable counting)
    - Duplicate content detection
    - Heading structure analysis (H1, H2, etc.)
    - Extraction of content from additional tags (`<strong>`, `<em>`, etc.)
- **Metadata Analysis**
    - Title tag extraction and validation
    - Meta description extraction and validation
    - Meta keywords extraction
    - Viewport meta tag validation
    - Robots meta tag validation
    - Canonical URL validation
    - OpenGraph data extraction and analysis (og:title, og:description, og:image, etc.)
    - Twitter Card data extraction and analysis (twitter:card, twitter:title, etc.)
- **URL Structure Analysis**
    - Scheme validation (HTTPS preferred)
    - Path analysis (length, character usage, keyword presence)
    - Query parameter analysis (identification, potential issues)
    - Fragment identifier analysis
    - URL length validation
    - Detection of common URL patterns (e.g., file extensions)
- **Link Analysis**
    - Identification of internal and external links
    - Anchor text analysis (length, descriptiveness)
    - Async checks for link status (broken links)
    - Async checks for redirects
    - Async checks for large file sizes linked
    - Analysis of link attributes (nofollow, target)
    - Normalization and classification of URLs (internal/external)
- **Image Analysis**
    - Alt tag presence and content analysis
    - Image dimension analysis
    - File size considerations
- **Mobile-Friendliness Assessment**
    - Viewport meta tag analysis
    - Touch target size and spacing analysis
    - Responsive image analysis (`srcset`, `sizes` attributes)
    - Font size analysis (readability on mobile)
    - Media query analysis (breakpoint coverage)
- **Performance Analysis**
    - Analysis of resource loading (scripts, stylesheets, images, fonts)
    - Script loading analysis (`async`, `defer`)
    - Stylesheet loading analysis
    - Image loading analysis (`loading="lazy"`)
    - Font loading analysis (`font-display`)
    - Critical rendering path analysis
    - Resource hint analysis (`preload`, `prefetch`, `preconnect`)
    - Caching header analysis (Cache-Control, Expires)
    - Cache busting techniques detection
    - Compression analysis (Content-Encoding)
    - Identification of critical resources
    - Above-the-fold content detection heuristics
    - TTFB and Total Load Time recording
    - Extraction of performance metrics from browser/headers
- **Security Analysis**
    - HTTPS usage check
    - Mixed content detection
    - Content Security Policy (CSP) header analysis
    - Form security analysis (autocomplete on sensitive fields)
    - External resource integrity analysis (SRI checks)
    - SSL certificate expiration check
- **Structured Data/Schema Markup Validation**
    - JSON-LD extraction and validation
    - Microdata extraction and validation
    - RDFa extraction and validation
    - Validation of schema properties against known types
    - Detection of deprecated schema properties
- **Web Vitals Metrics Analysis**
    - Analysis related to Largest Contentful Paint (LCP)
    - Analysis related to First Input Delay (FID) / Interaction to Next Paint (INP) precursors
    - Analysis related to Cumulative Layout Shift (CLS)
    - Analysis related to First Contentful Paint (FCP)
    - Analysis related to Time to Interactive (TTI)
    - Analysis related to Total Blocking Time (TBT)
    - Identification of blocking resources, long tasks, main thread work
    - Analysis of image dimensions, dynamic content, font loading impact
    - Calculation of an overall optimization score
    - Generation of specific recommendations based on metrics
- **CSS Analysis**
    - Identification of external and inline styles
    - Analysis of stylesheet content (potential issues, complexity)
    - Media query analysis (related to responsiveness)
    - Basic CSS-related accessibility checks
    - Basic CSS-related performance checks
    - Detection of potentially duplicate CSS rules
- **JavaScript Analysis**
    - Identification of external and inline scripts
    - Analysis of script attributes (`async`, `defer`)
    - Analysis of script loading patterns
    - Basic security checks
    - Analysis of inline script content complexity
    - Analysis of event handlers
    - Identification of third-party scripts
    - Basic checks for deprecated JS APIs
- **Internationalization Analysis**
    - Language declaration analysis (`lang` attribute)
    - `hreflang` implementation analysis
    - Character encoding analysis (UTF-8 preferred)
    - Text direction analysis (`dir` attribute)
    - Basic checks for locale-specific formatting issues
    - Basic checks for translation completeness heuristics
    - Basic checks for time zone handling heuristics
- **AI/LLM Analysis**
    - Integration with Anthropic API (requires API key)
    - Ability to send page content (or parts) to LLM for analysis based on predefined prompts
    - AI-Powered Content Recommendations
    - Automated Meta Description Generation
    - Title Tag Optimization Suggestions
    - Header Structure Recommendations
    - Content Expansion Suggestions
    - Executive Summary Generation

### Output Formats
- JSON output format
- JSONL (JSON Lines) output format
- XML output format
- CSV output format
- HTML report format
- Individual JSON files per page
- HTML folder output with index and individual page reports

### Reporting Features
- Detailed warnings and recommendations generated by individual analyzers
- Collection of page-level metadata
- Collection of page content details (headings, etc.)
- Collection of page resources (links, scripts, styles, images)
- Collection of Web Vitals analysis results
- Performance metrics reporting (TTFB, Load Time)
- Template-based HTML report generation

### Internationalization
- Multi-language support for UI text and report labels
- Built-in translations (English, Spanish, Chinese)
- Extensible translation system
- Locale used for specific recommendations

### Licensing System
- Trial mode with limited functionality
- Licensed mode with full functionality
- License validation system
- Different license tiers affecting functionality

### Technical Details
- Built in Rust and C++
- Asynchronous architecture
- HTML parsing and DOM manipulation
- Headless Chrome integration
- HTTP client
- Serialization/Deserialization
- Custom URL serialization wrapper
- Utility for creating safe filenames from URLs
- Command-line argument parsing
- Templating engine for HTML report generation

## Frequently Asked Questions

**What makes Black SEO Analyzer different from other SEO tools?**  
Unlike traditional SEO tools with browser-based interfaces and subscription models, Black SEO Analyzer is a tool that integrates directly into your development workflow. This approach enables automation capabilities that aren't possible with other tools, plus you genuinely own the software with a one-time purchase.

**How does the source code guarantee work?**  
Your purchase includes a legally-binding commitment that gives you access to the full source code if we ever discontinue the product, cease operations, or fail to provide updates for 12+ consecutive months. This ensures you can continue using the software indefinitely, regardless of our company's future.

**Can Black SEO Analyzer crawl JavaScript-heavy sites?**  
Yes, our integrated headless browser technology provides full JavaScript rendering capabilities. This ensures accurate analysis of modern web applications built with React, Angular, Vue.js, and other JavaScript frameworks.

**How are updates handled?**  
Updates are provided via our GitHub repository and can be downloaded at any time. You'll receive all future updates at no additional cost. Life-time ownership.
