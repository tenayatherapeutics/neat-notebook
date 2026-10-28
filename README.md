# <img src="https://raw.githubusercontent.com/tenayatherapeutics/neat-notebook/main/neat_notebook/tenaya-icon.png" alt="Tenaya Therapeutics" width="32" height="32"> Neat Notebook

[![CI](https://github.com/tenayatherapeutics/neat-notebook/actions/workflows/ci.yml/badge.svg)](https://github.com/tenayatherapeutics/neat-notebook/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/neat-notebook.svg)](https://pypi.org/project/neat-notebook/)
[![License: BSD-3-Clause](https://img.shields.io/badge/license-BSD--3--Clause-blue.svg)](https://github.com/tenayatherapeutics/neat-notebook/blob/main/LICENSE)

A lightweight cell inspector for **Jupyter Notebook 7** and **JupyterLab 4**.
See a cell's task, cursor position, execution status, elapsed time, and last-run
timestamp without losing your place. No kernel plugin, server extension, external
service, or JupyterLab rebuild is required.

Developed and maintained by [Farshad Farshidfar](https://github.com/farshadf)
([farshidfar@gmail.com](mailto:farshidfar@gmail.com)). This is an independently
maintained community extension, not an official Jupyter product.

![Inspector in Notebook's light theme](https://raw.githubusercontent.com/tenayatherapeutics/neat-notebook/main/docs/images/desktop-light.png)

## Installation

Install into the Python environment that runs your Jupyter server:

```sh
python -m pip install neat-notebook
```

To install Notebook as well:

```sh
python -m pip install 'neat-notebook[notebook]'
```

Restart Jupyter and reload the browser. End users installing the prebuilt wheel
do not need Node.js. Check discovery with `jupyter labextension list`.

| Component  | Supported range         |
| ---------- | ----------------------- |
| Python     | 3.11 or newer           |
| Notebook   | 7.5.6 or newer, below 8 |
| JupyterLab | 4.5.7 or newer, below 5 |

Notebook 6, NbClassic, and `jupyter_contrib_nbextensions` are not supported.
Notebook 7 uses the JupyterLab extension system. Existing host dependency bounds
must remain satisfied; do not use `--no-deps` to hide an installation conflict.

CI tests the minimum Notebook 7.5.6 / JupyterLab 4.5.7 pair on Python 3.11 and
Notebook 7.6.3 / JupyterLab 4.6.4 on Python 3.14. Browser tests run on Linux in
Chromium and Firefox. This is the tested compatibility matrix.

## Use

Select a cell in command or edit mode. Its inspector stays at the top of the
visible part of that cell, in a separate row above the input. It does not replace
the editor or existing cell-action toolbar.

- **Task:** click to edit; Enter or blur saves, Escape cancels, and clearing
  restores the automatic name. Automatic names use the first code comment
  starting with `#`, then a Markdown heading, then the cell type. Names update
  while typing, including `#Title` without a space.
- **Editor:** cell type, source-line count (one for an empty cell), and cursor
  position while the editor owns focus.
- **Execution:** Not run uses normal theme text, Running uses orange, Executed
  uses green, and Modified uses warning text. Status text accompanies color.
- **Timing:** live elapsed duration freezes on completion. Last run is shown in
  browser-local `HH:MM dd/mm/yyyy` format. Both are session-only and disappear
  after reload; the execution count still remains.
- **Narrow screens:** type, total lines, and last-run time move into a
  keyboard-accessible details disclosure. Timed states use a compact marker and
  timer. Wrapping occurs only when the contents no longer fit.

While execution is running, the inspector stays with that cell even when
Shift+Enter, Alt+Enter, or the Run button advances selection. Queuing another cell
does not displace it. On completion, error, or interruption it follows the next
running cell, or the selected cell if none are running. Focus remains controlled
by Jupyter. Kernel errors are still displayed by Jupyter's normal output area;
the inspector reflects execution state, not a separate success/error system.

Markdown and Raw cells are non-executable. Printing hides the inspector. The
extension uses the host's fonts and theme, provides keyboard focus styles, and
keeps per-second timer ticks outside its polite screen-reader live region.

Disable **Show Active Cell Inspector** under **Neat Notebook** in the host's
settings. It is enabled by default; the plugin ID is `neat-notebook:cell-inspector`.

### Other layouts

![Inspector in Notebook's dark theme](https://raw.githubusercontent.com/tenayatherapeutics/neat-notebook/main/docs/images/desktop-dark.png)

![Narrow inspector with details open](https://raw.githubusercontent.com/tenayatherapeutics/neat-notebook/main/docs/images/mobile.png)

These screenshots use synthetic notebooks from the browser test suite.

## Notebook data and privacy

Only explicit task-label edits write extension metadata:

```json
{
  "jupyter": {
    "cellInspector": {
      "task": "Prepare training data"
    }
  }
}
```

Other metadata, including `jupyter.source_hidden` and unrelated `cellInspector`
keys, is preserved. Clearing a label removes only its task value. Durations and
completion dates remain in memory; execution does not write timing metadata.
The extension has no telemetry, external API, or paid-service dependency.

## Troubleshooting and removal

- Confirm installation in the **server** environment, not only a kernel's
  environment, then restart Jupyter and reload the page.
- Check `python -m pip check` and `jupyter labextension list` before reporting
  missing or incompatible assets.

Uninstall with `python -m pip uninstall neat-notebook`, then restart Jupyter.
Saved task labels remain in notebook metadata, so uninstalling does not discard
your labels.

## Development and maintenance

See [CONTRIBUTING.md](https://github.com/tenayatherapeutics/neat-notebook/blob/main/CONTRIBUTING.md)
for local builds and tests, [RELEASING.md](https://github.com/tenayatherapeutics/neat-notebook/blob/main/RELEASING.md)
for protected publication, and [CHANGELOG.md](https://github.com/tenayatherapeutics/neat-notebook/blob/main/CHANGELOG.md)
for version history. Report bugs and focused feature requests through
[GitHub issues](https://github.com/tenayatherapeutics/neat-notebook/issues).

### Origin and license

Copyright © 2026 Tenaya Therapeutics. Developed and maintained by Farshad
Farshidfar. The project icon is the unmodified Tenaya Therapeutics favicon;
see [asset provenance](https://github.com/tenayatherapeutics/neat-notebook/blob/main/docs/images/README.md).

Neat Notebook originated in the active-cell inspector proposed in
[jupyter/notebook#8006](https://github.com/jupyter/notebook/pull/8006). Following
maintainer feedback, it is distributed independently. The BSD-3-Clause license
and original IPython/Jupyter notices are retained in
[LICENSE](https://github.com/tenayatherapeutics/neat-notebook/blob/main/LICENSE).
