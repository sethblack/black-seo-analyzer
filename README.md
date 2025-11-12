# Black SEO Analyzer

A professional tool for comprehensive SEO analysis, designed for SEO professionals that need their sites to be found in both search results and AI answers.

When run without a license you're limited in the number of pages you can crawl, but no other functionality is restricted. To purchase a license and unlock unlimited analysis power, visit [Black SEO Analyzer product page](https://www.blackseoanalyzer.com/).

![Black SEO Analyzer](https://www.sethserver.com/static/images/black-seo-analyzer.png)

## Overview

Black SEO Analyzer is a powerful command-line tool that keeps your website visible in both traditional search results and AI-generated responses. Good technical SEO isn't just about Google rankings - it's about making sure people can find your content when they need it.

When your site's structure and metadata are optimized correctly, you'll appear in both search results and AI conversations. Black SEO Analyzer cuts through the noise and tells you exactly what's holding your site back - without buzzwords, just actionable data how you need it.

## True Ownership

I'm tired of subscription-based tools that stop working when you stop paying. Black SEO Analyzer offers old-school (think the 80's and 90's) software ownership. Your purchase includes a legally-binding source code access guarantee if I ever discontinue the product - protecting your investment permanently.

**Black SEO Analyzer License: One-Time Purchase**
- Lifetime software ownership
- All future updates
- Command-line and GUI access with the same license
- Source code escrow guarantee
- Unlimited URLs and sites
- All advanced features included

## Installation

Please read the [INSTALL.md](INSTALL.md) file for installation instructions.

## Windows and Mac GUI

On Windows and Mac, Black SEO Analyzer includes a native graphical interface that provides an intuitive command-line experience within a modern, dark-themed window. The GUI offers the same powerful functionality as the command-line version with additional conveniences for GUI users.

### GUI Features

**Dark Theme Interface**
- Sweet-looking dark color scheme optimized for extended viewing
- Color-coded output with full ANSI escape sequence support
- Real-time streaming output with automatic scrolling

**Intelligent Command Input**
- **Command History**: Navigate previous commands with Up/Down arrow keys
- **Auto-completion**: Type-ahead suggestions for all built-in commands
  - Accept with Tab or Right Arrow
  - Covers commands like `crawl`, `set`, `show config`, `export`, `license`, etc.
- **Smart Focus**: Type anywhere in the window—input field automatically receives focus
- **Command Echo**: All executed commands displayed in yellow with `>` prompt

**Native Integration**
- **File Dialogs**: Save/load configuration files with standard dialogs
- **Folder Browser**: Native folder selection for output directories
- **Icons & Graphics**: Application icon and modern UI elements
- **Clipboard Support**: Copy output text to clipboard

**Configuration Management**
All configuration options accessible through text commands. For example:
```
set url https://example.com
set output-dir C:\SEO\Reports
set concurrent-requests 20
set rate-limit 100
show config
save my-config.json
```

**Supported Commands in GUI**
- `help` - Display comprehensive command help
- `version` - Show application version
- `crawl [url]` - Start SEO analysis
- `set <option> <value>` - Configure settings
- `show config` - Display current configuration
- `save [filename]` - Save configuration to JSON
- `load [filename]` - Load configuration from JSON
- `license [key]` - Set or check license status
- `list crawls` - View all previous crawl sessions
- `export <session_id> [format]` - Export crawl results from database
- `clear` - Clear output display
- `exit` / `quit` - Close application

**Real-Time Crawl Feedback**
- Live output streaming as crawler analyzes pages
- Color-coded status messages (errors in red, success in green, warnings in yellow)
- Progress updates with page counts and timing information

**Database Operations**
- List all previous crawl sessions with details (session ID, URL, dates, page count)
- Export any previous crawl to various formats (JSON, XML, CSV, HTML)
- Pre-export diagnostics with detailed error reporting
- SQLite database managed automatically in output directory

**AI Integration Support**
Configure AI-powered analysis directly from GUI:
- Anthropic Claude (claude-3-5-sonnet-20241022 default)
- OpenAI GPT (gpt-4o default)
- DeepSeek (deepseek-chat default)
- Google Gemini (gemini-2.0-flash-exp default)

Set API keys and custom prompts via commands:
```
set anthropic-api-key YOUR_KEY
set openai-model gpt-4o
set anthropic-prompt-file prompts\custom-seo.txt
```

**Semantic Analysis**
Enable vector-based semantic content analysis:
```
set enable-semantic-analysis true
set semantic-query "e-commerce best practices"
set semantic-similarity-threshold 0.75
```

### GUI Benefits Over Command-Line

- **Visual Feedback**: See colorized output in real-time
- **Easier Configuration**: Set options with simple commands rather than long parameter lists
- **Persistent Settings**: Save/load configuration files with dialog boxes
- **History Navigation**: Recall previous commands instantly
- **Auto-completion**: Discover commands as you type
- **Database Browsing**: List and export previous crawls interactively
- **No Terminal Required**: Self-contained application window

## Windows CLI Usage

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
          Optional path to custom HTML templates directory
      --headless
          Run in headless mode without launching the GUI [experimental] defaults to true
  -h, --help
          Print help
  -V, --version
          Print version
```

### Windows CLI Example Usage

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

## Linux/MacOS CLI Usage

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
          Optional path to custom HTML templates directory
      --headless
          Run in headless mode without launching the GUI [experimental] defaults to true
  -h, --help
          Print help
  -V, --version
          Print version
```

### Linux/MacOS CLI Example Usage

Notes:

* If the binary is not executable, you may need to run `chmod +x ./black-seo-analyzer` first.
* The examples below assume the binary is in the current directory. If it's in a different directory, you'll need to provide the full path to the binary or if it is in your PATH, you can just run `black-seo-analyzer`.

#### Basic JSON output for one site
```bash
./black-seo-analyzer --url-to-begin-crawl https://example.com --output-type json --output-file example-report.json
```

#### Website with a sitemap
```bash
./black-seo-analyzer --url-to-begin-crawl https://example.com/sitemap.xml --is-sitemap --output-type json --output-file sitemap-report.json
```

#### Single page app
```bash
./black-seo-analyzer --url-to-begin-crawl https://spa-example.com --spa --output-type json --output-file spa-report.json
```

#### HTML folder output
```bash
./black-seo-analyzer --url-to-begin-crawl https://example.com --output-type html-folder --output-file ./seo-reports
```

## Comprehensive Feature List

### Core Functionality
- Command-line interface
- Windows GUI with native dialogs and dark theme
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
- Built with Rust
- Windows GUI built with MFC (Microsoft Foundation Classes)
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
Unlike traditional SEO tools with browser-based interfaces and subscription models, Black SEO Analyzer is a command-line tool that integrates directly into your development workflow. This approach enables automation capabilities that aren't possible with other tools, plus you genuinely own the software with a one-time purchase.

**How does the source code guarantee work?**  
Your purchase includes a legally-binding commitment that gives you access to the full source code if we ever discontinue the product, cease operations, or fail to provide updates for 12+ consecutive months. This ensures you can continue using the software indefinitely, regardless of our company's future.

**Can Black SEO Analyzer crawl JavaScript-heavy sites?**  
Yes, our integrated headless browser technology provides full JavaScript rendering capabilities. This ensures accurate analysis of modern web applications built with React, Angular, Vue.js, and other JavaScript frameworks.

**How are updates handled?**  
Updates are provided via our GitHub repository and can be downloaded at any time. You'll receive all future updates at no additional cost. Life-time ownership.

**Does the Windows version have a GUI?**  
Yes! Both Windows and Mac have intuitive command-line interfaces built within a modern, dark-themed window. The GUI includes command history, auto-completion, native file dialogs, and real-time color-coded output. You can still use the traditional command-line interface if you prefer.

**Can I use both the GUI and command-line versions?**  
Absolutely. Both share the same configuration files and database, so you can switch between them seamlessly even across platforms.
