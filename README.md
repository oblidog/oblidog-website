# Oblidog Website

Static landing page for [Oblidog](https://github.com/oblidog/oblidog-ledger).

## Local preview

Run any static HTTP server from the repository root, for example:

```bash
python3 -m http.server 8000
```

Then open [http://localhost:8000](http://localhost:8000).

## Deployment

The site is intentionally buildless: deploy the repository root as static assets.

## Product screenshots

The images are real application captures with sample data from the Ledger
[Demo Screenshots workflow](https://github.com/oblidog/oblidog-ledger/actions/workflows/demo-screenshots.yml).
The current set comes from [run 43135344604](https://github.com/oblidog/oblidog-ledger/actions/runs/43135344604),
commit `b2a1463d35c8b387cc4ca15e3d90f7dc12d3436c` (12 November 2026).

- `desktop-dark.png` / `desktop-light.png`: 1440 × 1000 obligations views.
- `mobile-light.png`: 390 × 844 obligations view.
- `dashboard-payments-desktop-light.png`: 1120 × 567 calendar and forecast.
- `dashboard-payments-mobile-light.png`: 358 × 1217 calendar and forecast.

Refresh these files together from a successful capture run. Update the HTML
image dimensions if they change. The hero crops the desktop image vertically
and focuses the mobile image on the bill cards; the original files remain intact.
The calendar uses a separate mobile capture so its labels stay readable.

After editing, check desktop and mobile widths, image loading, anchor navigation,
keyboard focus, and the demo/documentation links. There is no build step or
JavaScript dependency. Workflow copy should match the Ledger
[obligation lifecycle](https://github.com/oblidog/oblidog-ledger/blob/main/docs/obligation-lifecycle.md).
The four-stage timeline is an example path, not a mandatory sequence. Integration
copy links to the API, Python SDK, and demo adapter as a starting point for custom
integrations; it does not advertise individual providers or an installable template.
