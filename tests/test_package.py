"""Validate the installed prebuilt distribution, rather than development links."""

import json
from importlib.metadata import distribution
from pathlib import Path

from packaging.requirements import Requirement

import neat_notebook


def test_version():
    package = json.loads((Path(__file__).resolve().parents[1] / "package.json").read_text())
    assert neat_notebook.__version__ == distribution("neat-notebook").version == package["version"]


def test_public_metadata():
    metadata = distribution("neat-notebook").metadata
    assert metadata["Author-email"] == "Farshad Farshidfar <farshidfar@gmail.com>"
    assert metadata["Maintainer-email"] == "Farshad Farshidfar <farshidfar@gmail.com>"
    assert "Framework :: Jupyter :: JupyterLab :: Extensions :: Prebuilt" in metadata.get_all(
        "Classifier"
    )
    assert "Source, https://github.com/tenayatherapeutics/neat-notebook" in metadata.get_all(
        "Project-URL"
    )


def test_company_attribution_and_icon():
    dist = distribution("neat-notebook")
    license_path = next(path for path in dist.files or [] if str(path).endswith("/LICENSE"))
    license_text = Path(dist.locate_file(license_path)).read_text()
    assert "Copyright (c) 2026, Tenaya Therapeutics" in license_text
    assert "IPython Development Team" in license_text
    assert "Jupyter Development Team" in license_text
    icon = Path(neat_notebook.__file__).parent / "tenaya-icon.png"
    assert icon.read_bytes()[:24] == (
        b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x20\x00\x00\x00\x20"
    )


def test_supported_host_dependencies():
    requirements = {
        requirement.name: requirement
        for value in distribution("neat-notebook").requires or []
        if (requirement := Requirement(value)).name in {"jupyterlab", "notebook"}
    }
    lab = requirements["jupyterlab"]
    assert lab.marker is None
    assert "4.5.7" in lab.specifier
    assert "4.6.4" in lab.specifier
    assert "5.0.0" not in lab.specifier
    notebook = requirements["notebook"]
    assert notebook.marker is not None
    assert notebook.marker.evaluate({"extra": "notebook"})
    assert not notebook.marker.evaluate({"extra": ""})
    assert "7.5.6" in notebook.specifier
    assert "7.6.3" in notebook.specifier
    assert "8.0.0" not in notebook.specifier


def test_discovery():
    assert neat_notebook._jupyter_labextension_paths() == [
        {"src": "labextension", "dest": "neat-notebook"}
    ]


def test_frontend_assets():
    dist = distribution("neat-notebook")
    files = list(dist.files or [])
    package = next(
        path for path in files if str(path).endswith("labextensions/neat-notebook/package.json")
    )
    root = Path(dist.locate_file(package)).parent
    metadata = json.loads((root / "package.json").read_text())
    assert metadata["name"] == "neat-notebook"
    assert metadata["version"] == neat_notebook.__version__
    assert (root / metadata["jupyterlab"]["_build"]["load"]).is_file()
    assert (root / "static/style.js").is_file()
    schema = json.loads((root / "schemas/neat-notebook/cell-inspector.json").read_text())
    assert schema["properties"]["enabled"]["default"] is True
    install = json.loads((root / "install.json").read_text())
    assert install["packageName"] == "neat-notebook"


def test_singleton_dependencies_and_duplicate_prevention():
    dist = distribution("neat-notebook")
    package = next(
        path
        for path in dist.files or []
        if str(path).endswith("labextensions/neat-notebook/package.json")
    )
    metadata = json.loads(Path(dist.locate_file(package)).read_text())
    assert metadata["jupyterlab"]["disabledExtensions"] == [
        "@jupyter-notebook/notebook-extension:cell-inspector"
    ]
    for dependency in metadata["jupyterlab"]["sharedPackages"].values():
        assert dependency == {"singleton": True, "bundled": False}
