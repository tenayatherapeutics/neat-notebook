# Contributing

Developer and maintainer: [Farshad Farshidfar](https://github.com/farshadf),
[farshidfar@gmail.com](mailto:farshidfar@gmail.com).

Open an issue before a substantial feature or architectural change so scope and
compatibility can be discussed. Small fixes can go directly to a pull request.
Contributions are distributed under this repository's BSD-3-Clause license.
Please follow [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## Local development

Use an isolated Python environment with Python 3.11+ and Node.js 22.13+ or 24+. Activate it
before every development session. Do not change a production Jupyter environment
or copy credentials into the repository.

```sh
python -m pip install 'jupyter-builder>=1.2.4,<2' build 'ruff>=0.16.1,<0.17' twine
jlpm install --immutable
jlpm lint:check
jlpm test:types
jlpm build:prod
python -m build
python -m twine check --strict dist/*
python -m pip install '.[dev]'
```

The source distribution includes prebuilt assets. `python -m build` builds the
wheel from that source distribution, not just from the working tree. `jlpm` is
provided by `jupyter-builder`; no separate global Yarn installation is required.
The project has no Makefile or Rust component. Use its native build commands.
Build resolutions select the published JupyterLab 4.6.4 SDK rather than partially
published prereleases. Update these pins and the lockfile together with host tests.

For iterative development, link the built assets with
`jupyter-builder develop . --overwrite`, rebuild after changes, and refresh
Notebook or JupyterLab. Do not use a development link for release validation.

## Validate the installed wheel

Install a wheel into a separate environment containing a compatible Notebook,
JupyterLab, ipykernel, pytest, and pytest-xdist. For example, using a wheel built
above:

```sh
python -m venv /tmp/neat-host
/tmp/neat-host/bin/python -m pip install \
  'notebook==7.5.6' 'jupyterlab==4.5.7' ipykernel pytest pytest-xdist \
  dist/neat_notebook-0.1.4-py3-none-any.whl
/tmp/neat-host/bin/python -m pip check
```

Run the distribution tests from outside this checkout so Python imports the
installed package rather than the source directory:

```sh
# Replace /absolute/path/to/neat-notebook with your checkout path.
cd /tmp
/tmp/neat-host/bin/python -m pytest -n 12 /absolute/path/to/neat-notebook/tests
```

On Windows use the environment's `Scripts/python.exe` instead of `bin/python`.
Use a unique temporary environment path if `/tmp/neat-host` already exists.

From the project root, run the real-kernel browser tests:

```sh
jlpm exec playwright install chromium firefox
NEAT_NOTEBOOK_PYTHON=/tmp/neat-host/bin/python jlpm test:ui --workers=4
```

Linux CI installs browser system dependencies with `playwright install --with-deps`.
Each test server gets its own temporary notebook, config, data, and runtime
directories. Only loopback test servers are unauthenticated. Never deploy
`ui-tests/jupyter_server_config.py` as a real server configuration.

The suite measures a Neat-disabled baseline before classifying the documented
Notebook 7.6.3 startup issue. Do not broaden that exception or suppress page
errors to make a test pass. All unexpected browser errors must fail.

## Scope and review checklist

- Keep the extension small. Reuse Jupyter services, theme variables, and public
  models rather than introducing a separate application framework.
- Preserve task metadata compatibility and unrelated cell metadata. Timing must
  remain session-only; do not write timestamps just because a cell executes.
- Test selection changes, queuing, completion, errors, interrupts, deletion, and
  disposal. Keep timer cleanup and signal disconnection explicit.
- Cover keyboard access, live-region behavior, both themes, narrow layouts, and
  printing when changing UI. Follow [DESIGN.md](DESIGN.md).
- Update documentation and the changelog. Review generated screenshots before
  accepting visual changes; do not mask an unexpected regression.
- Never submit sensitive notebooks or production data as fixtures.

CI tests minimum and current supported host pairs using the same built wheel.
New host releases should be evaluated before changing the documented matrix.
Use `jlpm format` for formatting, and rerun `jlpm lint:check` afterward.

Publication is a separate, protected operation. See [RELEASING.md](RELEASING.md).
