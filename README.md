# Black SEO Analyzer

A professional command-line tool for comprehensive SEO analysis, designed for websites that need to be found in both search results and AI answers.

![Black SEO Analyzer](https://www.sethserver.com/static/images/code.png)

To purchase a license, visit the [Black SEO Analyzer product page](https://www.sethserver.com/seo/black-seo-analyzer.html).

## Overview

Black SEO Analyzer is a powerful command-line tool that keeps your website visible in both traditional search results and AI-generated responses. In today's digital landscape, good technical SEO isn't just about Google rankings—it's about making sure AI systems can find and understand your content when people ask about your industry.

When your site's structure and metadata are optimized correctly, you'll appear in both search results and AI conversations. Black SEO Analyzer cuts through the noise and tells you exactly what's holding your site back - without corporate buzzwords, just actionable data so you don't get left behind when someone asks an AI about exactly what you sell.

## Key Features

- **Crawl Any Website Architecture**: Analyze standard websites or modern Single-Page Applications with ease. Our headless browser integration ensures complete analysis of JavaScript-rendered content and modern frameworks.

- **Validate All Metadata & Structured Data**: Identify issues with page titles, meta descriptions, OpenGraph tags, Twitter Cards, and Schema.org implementations for both search engines and AI answer engines.

- **Discover Content Issues & Opportunities**: Analyze content quality with readability scoring, heading structure validation, and keyword optimization suggestions. Identify thin content and duplicate pages.

- **Fix Technical SEO Problems**: Find broken links, redirect chains, and server errors. Validate your robots.txt, XML sitemaps, and canonicalization to ensure proper crawling and indexing.

- **Measure Core Web Vitals & Performance**: Assess critical performance metrics including LCP, CLS, FID, and more. Get actionable recommendations to improve page speed and user experience.

- **Generate Comprehensive Reports**: Export detailed reports in multiple formats (JSON, CSV, XML, HTML) to fit your workflow. Integrate results directly into your development pipeline.

## True Ownership, Not Subscription

Unlike subscription-based tools that stop working when you stop paying, Black SEO Analyzer offers genuine software ownership. Your purchase includes a legally-binding source code access guarantee if we ever discontinue the product — protecting your investment permanently.

**Black SEO Analyzer License: $259 One-Time Purchase**
- Lifetime software ownership
- All future updates
- Command-line efficiency
- Source code escrow guarantee
- Unlimited URLs and sites
- All advanced features included

## Installation

1. Download the appropriate executable for your operating system from the [releases page](https://github.com/sethblack/black-seo-analyzer/releases).
2. Make the file executable (Linux/macOS): `chmod +x black-seo-analyzer`
3. Move to a directory in your PATH for easy access (optional)

## Usage

```
Usage: black-seo-analyzer.exe [OPTIONS] --url-to-begin-crawl <URL_TO_BEGIN_CRAWL>

Options:
      --url-to-begin-crawl <URL_TO_BEGIN_CRAWL>
          URL of the sitemap to analyze
      --log-file <LOG_FILE>
          Path to log file
      --output-type <OUTPUT_TYPE>
          Output format type [default: html-folder] [possible values: json, jsonl, xml, csv, csv-flat, html-folder]
      --concurrent-requests <CONCURRENT_REQUESTS>
          Optional Number of concurrent requests to make [default: 20]
      --rate-limit <RATE_LIMIT>
          Optional Rate limit in milliseconds [default: 50]
      --output-file <OUTPUT_FILE>

      --spa

      --is-sitemap

      --locale <LOCALE>
          Optional locale for internationalization [default: en]
  -h, --help
          Print help
  -V, --version
          Print version
```

### Example Usage

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

## Real-World Applications

### Automated SEO Monitoring

```bash
# Weekly site audit with email notification for critical issues
0 0 * * 1 /usr/local/bin/black-seo-analyzer.exe --url-to-begin-crawl example.com --output-type json \
| /usr/local/bin/seo-alert-filter \
| mail -s "Weekly SEO Report" team@example.com
```

### CI/CD Pipeline Integration

```yaml
# In your GitHub Actions workflow
seo_validation:
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v3
    - name: Run SEO Analysis
      run: |
        black-seo-analyzer.exe --url-to-begin-crawl https://staging.example.com \
        --output-type json --output-file seo-report.json
    - name: Validate Critical SEO Elements
      run: |
        cat seo-report.json | jq '.pages[] | select(.errors | length > 0)' > critical-errors.json
        if [ -s critical-errors.json ]; then
          echo "SEO validation failed - see critical-errors.json"
          exit 1
        fi
```

### Bulk Site Analysis

```bash
# Analyze multiple sites and combine reports
for site in site1.com site2.com site3.com; do
  black-seo-analyzer.exe --url-to-begin-crawl $site --output-type json --output-file "${site}.json"
done

# Combine results for comparison
jq -s '[.[] | {site: .site, score: .score, errorCount: .errorCount}]' *.json > summary.json
```

### Content Optimization Workflow

```bash
# Extract all H1 tags and meta descriptions for content review
black-seo-analyzer.exe --url-to-begin-crawl example.com --output-type csv-flat \
| grep -E "(h1|meta_description)" \
| sort -t',' -k2 \
> content-review.csv
```

## Advanced Features

- **SPA Rendering**: Full support for JavaScript-rendered sites with headless Chrome integration, dynamic content waiting and extraction, network idle detection, and retry mechanisms for reliable content extraction.

- **Resource Analysis**: Detailed assessment of all page resources including image optimization assessment, script and stylesheet optimization suggestions, font loading strategy evaluation, and resource prioritization analysis.

- **Comprehensive Reporting**: Clear, actionable insights with detailed page-level analysis, site-wide issue aggregation, prioritized recommendations, performance scoring, and visual HTML reports.

- **Internationalization**: Global SEO support with built-in translations (English and Spanish), extensible translation system, locale-specific analysis and reporting, hreflang tag validation, and language-specific content assessment.

## Frequently Asked Questions

**What makes Black SEO Analyzer different from other SEO tools?**  
Unlike traditional SEO tools with browser-based interfaces and subscription models, Black SEO Analyzer is a command-line tool that integrates directly into your development workflow. This approach enables automation capabilities that aren't possible with other tools, plus you genuinely own the software with a one-time purchase.

**How does the source code guarantee work?**  
Your purchase includes a legally-binding commitment that gives you access to the full source code if we ever discontinue the product, cease operations, or fail to provide updates for 12+ consecutive months. This ensures you can continue using the software indefinitely, regardless of our company's future.

**Can Black SEO Analyzer crawl JavaScript-heavy sites?**  
Yes, our integrated headless browser technology provides full JavaScript rendering capabilities. This ensures accurate analysis of modern web applications built with React, Angular, Vue.js, and other JavaScript frameworks.

**How are updates handled?**  
Updates are provided via our GitHub repository and automatically checked by the tool itself. When new versions are available, you'll be notified when running the program. You'll receive all future updates at no additional cost.