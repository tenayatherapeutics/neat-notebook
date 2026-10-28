# Changelog

## 0.1.4 — prepared for the first public release

- Extracted the tested extension into `tenayatherapeutics/neat-notebook`, without
  changing the inspector's UI or execution behavior.
- Added developer/maintainer metadata for Farshad Farshidfar and public project URLs.
- Added independent lint/type/build checks, locked JavaScript dependencies, and
  installed-wheel/browser CI for Notebook 7.5.6 and 7.6.3 with their compatible
  JupyterLab versions.
- Added contribution, security, maintenance, and release documentation with
  synthetic screenshots.
- Prepared manual, protected PyPI/TestPyPI Trusted Publishing workflows.

This version is not published until the registry release is approved and verified.

## Local previews 0.1.0–0.1.3

Developed in `tenayatherapeutics/notebook` following
[jupyter/notebook#8006](https://github.com/jupyter/notebook/pull/8006).

- Active/running cell inspector with task editing, live automatic labels, source
  line counts, focused-editor cursor position, and responsive details.
- Monotonic execution timing, frozen duration, and browser-local completion
  timestamps retained only for the session.
- Theme-aware status colors, keyboard access, polite state announcements,
  printing support, and settings-based disabling.
- Running-cell pinning, queued execution handoff, and disposal cleanup.
- Corrected the initial preview's host dependency incompatibility for Notebook 7.5.

The extraction starts from source commit `04ad8467b`. These previews were locally
distributed wheels, not public PyPI or npm releases.
