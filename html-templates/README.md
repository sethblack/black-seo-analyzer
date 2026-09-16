# HTML report templates

These are the templates Black SEO Analyzer compiles into the binary to produce
its HTML reports. Copy the ones you want to change into a directory of your own
and point the analyzer at it:

```sh
bseoa crawl --url-to-begin-crawl https://example.com \
  --output-type html-folder \
  --html-templates-dir ./my-templates
```

`bseoa export --output-type html-folder --html-templates-dir ./my-templates`
takes the same flag, as do `--output-type sitemap` and `--output-type
topic-cluster`.

## Rules

- Only the filenames listed below are recognized. A file with any other name is
  ignored.
- You only need to supply the templates you want to change. Anything the
  directory does not contain is taken from the built-in copy.
- A directory that holds none of these filenames is rejected with an error
  rather than silently ignored, and so is a directory that does not exist.
- A template that fails to parse aborts the export and names the file it came
  from.
- There is no asset pipeline. CSS, JavaScript and images must be inlined in the
  template or referenced by absolute URL.

## Engine

The reports render with [Tera](https://keats.github.io/tera/) 2, which follows
Jinja2 closely but not exactly. The differences that bite most often:

- Filter arguments are keyword arguments: `{{ score | round(precision=1) }}`,
  not `{{ score | round(1) }}`.
- Slicing uses Python-style syntax — `{% for k in keyword_analysis[:50] %}` —
  and the Tera 1 `slice` filter no longer exists.
- `{% if x %}` on an undefined variable is false rather than an error, so
  guarding optional sections with `{% if %}` is safe.

## Files

| File | Renders |
| --- | --- |
| `index_file.html` | `index.html`, the crawl summary at the root of the export |
| `page_file.html` | the wrapper document for each file under `pages/` |
| `page.html` | the report body, inserted into `page_file.html` as `page_content`, and the whole document for single-page output |
| `sitemap_graph.html` | `--output-type sitemap` |
| `topic_cluster_graph.html` | `--output-type topic-cluster` |

The folder export writes `index.html` plus one file per page under `pages/`.
Visualization JSON, when enabled, is written to `visualizations/`.

## Context: `index_file.html`

| Variable | Type |
| --- | --- |
| `date` | string, when the export ran |
| `total_pages` | integer |
| `total_issues` | integer |
| `avg_issues` | float, issues per page |
| `top_pages` | up to 10 `{ url, filename, issues }`, most issues first |
| `sorted_pages` | every internal page as `{ url, filename, issues }`, by path depth |
| `keyword_analysis` | site-wide `{ keyword, score }`, highest score first |

`filename` is the name under `pages/`, without the `.html` suffix.

## Context: `page_file.html`

| Variable | Type |
| --- | --- |
| `url` | string |
| `title` | string |
| `page_content` | the rendered `page.html` output; insert it with `{{ page_content | safe }}` |

## Context: `page.html`

Everything here is optional — guard each section with `{% if %}`.

| Variable | Type |
| --- | --- |
| `url`, `date`, `title`, `description`, `author`, `hostname`, `sitename` | string |
| `og_title`, `og_description`, `og_image` | string |
| `twitter_title`, `twitter_description`, `twitter_image` | string |
| `has_social_media` | bool, true when any `og_*`/`twitter_*` value is present |
| `total_word_count` | integer |
| `internal_links`, `external_links`, `images`, `scripts`, `stylesheets` | list of URL strings |
| `warnings` | list of `{ message, link }`; folder exports also carry `key` and `severity` |
| `keyword_analysis` | list of `{ keyword, score }`, highest score first |
| `web_vitals_score` | float |
| `web_vitals_metrics` | map of name to `{ name, value, rating, issues }` |
| `web_vitals_recommendations` | list of strings |
| `ssl_expiration_date` | string |
| `has_accessibility_analysis`, `accessibility_analysis` | `{ score, violations }` |
| `has_anthropic_analysis`, `anthropic_analysis` | `{ raw_response, recommendations }` |
| `has_openai_analysis`, `openai_analysis` | same shape |
| `has_deepseek_analysis`, `deepseek_analysis` | same shape |
| `has_gemini_analysis`, `gemini_analysis` | same shape |

Each entry in `accessibility_analysis.violations` is
`{ key, guideline, message, element, link, location }`, where `location`, when
present, is `{ line, column }`.

`raw_response` is the model's reply as Markdown, with one exception: in
single-page output the OpenAI reply is converted to HTML first, which is why the
built-in template emits that one with `| safe` and the others inside `<pre>`.

## Context: the graph templates

`sitemap_graph.html` and `topic_cluster_graph.html` are **not** Tera templates.
They are emitted verbatim except for the literal string `{json_data}`, which is
replaced with the graph as JSON. Keep that placeholder somewhere the page's
JavaScript can read it.

For `sitemap_graph.html` the JSON is `{ nodes, links }` where a node is
`{ id, group, status, url, title, description, image }` — `group` is crawl depth
— and a link is `{ source, target, value }`.

For `topic_cluster_graph.html` it is `{ nodes, links }` where a node is
`{ id, group, url, title, description, image }` — `group` is the cluster it
belongs to — and a link is `{ source, target, value }`, `value` being the
similarity score between the two pages.
