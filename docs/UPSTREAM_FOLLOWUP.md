# Prepared upstream follow-up — not posted

Use this only after the first public PyPI release is available and the maintainer
approves posting to [jupyter/notebook#8006](https://github.com/jupyter/notebook/pull/8006).
Closing or changing that PR is a separate maintainer decision.

---

Thanks @jtpio and @krassowski for recommending a standalone extension. I have
extracted the cell inspector into **Neat Notebook**, an independently maintained
prebuilt extension for Notebook 7 and JupyterLab 4:

- Repository and screenshots: https://github.com/tenayatherapeutics/neat-notebook
- Installation: `python -m pip install neat-notebook`
- Compatibility: Python 3.11+, Notebook >=7.5.6,<8, and JupyterLab >=4.5.7,<5.
- CI builds and tests the installed wheel on stock Notebook/JupyterLab in both
  Chromium and Firefox, including keyboard access, themes, narrow layouts,
  execution timing, and lifecycle cleanup.

The extension does not require a Notebook fork, kernel/server plugin, or core
patch. It uses Jupyter's existing services and models, preserves unrelated cell
metadata, and keeps execution timing session-local. I will maintain it through
the new repository. I am happy to propose a separately scoped core change if a
missing extension point becomes a concrete obstacle.

This follows the standalone-extension direction rather than asking to include
the feature in Notebook core. Thank you for the guidance.
