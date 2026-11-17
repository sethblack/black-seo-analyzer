# Black SEO Analyzer GitHub Action

Crawl a site on every pull request and fail the build when a change introduces
new technical SEO or AI-readiness issues.

The point of the baseline is that a pull request is judged on what it *changed*.
Without one, every run reports the whole backlog and `fail-on` is unusable on
any site that isn't already clean.

## Quick start

```yaml
- uses: sethblack/black-seo-analyzer/integrations/github-action@v26.11.18
  with:
    url: https://preview.example.com
    license-key: ${{ secrets.BSEOA_LICENSE_KEY }}
    fail-on: high
```

That fails the job if the crawl finds anything at `high` or `critical` —
including pre-existing issues. Add a baseline to report only what the branch
introduced.

## Pull requests, compared against `main`

```yaml
name: SEO
on: pull_request

jobs:
  audit:
    runs-on: ubuntu-latest
    steps:
      - name: Restore the baseline crawl
        id: baseline
        uses: actions/cache/restore@v4
        with:
          path: baseline.db
          key: bseoa-baseline-${{ github.base_ref }}

      - name: Audit the preview deployment
        uses: sethblack/black-seo-analyzer/integrations/github-action@v26.11.18
        with:
          url: ${{ steps.deploy.outputs.preview-url }}
          license-key: ${{ secrets.BSEOA_LICENSE_KEY }}
          baseline: baseline.db
          fail-on: high
          max-pages: 100
```

Refresh the baseline when `main` moves, so the next pull request is compared
against what actually shipped:

```yaml
name: SEO baseline
on:
  push:
    branches: [main]

jobs:
  baseline:
    runs-on: ubuntu-latest
    steps:
      - uses: sethblack/black-seo-analyzer/integrations/github-action@v26.11.18
        id: audit
        with:
          url: https://example.com
          license-key: ${{ secrets.BSEOA_LICENSE_KEY }}
          db-path: baseline.db
          max-pages: 500
          # No fail-on: this run records the state of main, it does not judge it.

      - uses: actions/cache/save@v4
        with:
          path: baseline.db
          key: bseoa-baseline-${{ github.ref_name }}
```

## Inputs

| Input | Default | Description |
|---|---|---|
| `url` | — | **Required.** The URL to crawl, usually a preview deployment. |
| `license-key` | — | **Required.** Pass from a secret. [Free 14-day trial](https://www.blackseoanalyzer.com/free-trial). |
| `version` | `latest` | Release to download, e.g. `26.9.16`. |
| `max-pages` | `100` | Stop after this many pages. |
| `fail-on` | *(none)* | `low`, `medium`, `high` or `critical`. Empty reports without failing. |
| `audit-profile` | `full` | `full`, `standard`, `core`, `critical`, `quick`. Hyphenated forms such as `quick-scan` also work. |
| `crux-api-key` | *(none)* | Chrome UX Report key, from a secret. Adds Core Web Vitals as real users measured them. |
| `baseline` | *(none)* | An earlier crawl database. Turns `fail-on` into "new issues only". |
| `db-path` | `bseoa-crawl.db` | Where to write the crawl database. |
| `summary` | `true` | Write a report to the job summary. |

Only `full` runs the AI-readiness checks — the robots.txt AI-crawler audit,
llms.txt, and the render gap. They are tier 4, like Security and Mobile, so the
narrower profiles skip them.

### Field performance data

With `crux-api-key` set, the crawl asks the Chrome UX Report what real Chrome
users measured over the last 28 days, for the site as a whole and for up to 50
of its shallowest pages. A page that fails LCP, INP or CLS for real users is an
issue like any other, so `fail-on` and the baseline diff apply to it.

CrUX only reports pages with enough traffic, so a preview deployment has no
field data of its own. It is most useful in the baseline job against
production. The key is free from a Google Cloud project with the Chrome UX
Report API enabled.

## Outputs

| Output | Description |
|---|---|
| `database` | The crawl database this run produced. |
| `report` | JSON report: the diff when a baseline was used, otherwise every issue. |
| `session-id` | This run's crawl session id. |
| `compared-against` | The earlier session id, empty when there was no baseline. |

## Exit codes

The action fails the job with the CLI's own codes:

| Code | Meaning |
|---|---|
| 0 | Clean, or findings below `fail-on`. |
| 1 | The crawl itself failed. |
| 3 | Licence missing, invalid or expired. |
| 4 | `fail-on` threshold met. |

## Runners

Linux, macOS and Windows runners are all supported; the right release binary is
chosen from `RUNNER_OS`. Linux is the cheapest and the fastest to start.

`python3` must be on `PATH`, which it is on all three GitHub-hosted images.

## Notes

The licence key is passed to the CLI through the environment, never on a
command line, so it does not appear in process listings or shell traces. Keep
it in a repository or organisation secret.

A first run with no cached baseline is not an error: the action says so and
reports every issue instead of only the new ones.
