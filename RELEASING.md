# Releasing Neat Notebook

Release owner: Farshad Farshidfar
([@farshadf](https://github.com/farshadf), farshidfar@gmail.com).

The `Publish` workflow is manual. Pushes, pull requests, tags, and GitHub releases
do not upload packages. Each registry deployment requires approval from
`farshadf` in GitHub Actions.

## Registry accounts and publishers

**PyPI and TestPyPI require separate accounts and separate Trusted Publishers.**
An account or publisher on one service does not exist on the other service.
Both projects are configured for this repository:

| Registry | Publisher settings                                                                                  | GitHub environment |
| -------- | --------------------------------------------------------------------------------------------------- | ------------------ |
| PyPI     | [neat-notebook publishers](https://pypi.org/manage/project/neat-notebook/settings/publishing/)      | `pypi`             |
| TestPyPI | [neat-notebook publishers](https://test.pypi.org/manage/project/neat-notebook/settings/publishing/) | `testpypi`         |

Both registrations use GitHub owner `tenayatherapeutics`, repository
`neat-notebook`, and workflow filename `publish.yml`. The environment must match
the selected registry. Publishing uses short-lived OIDC credentials; no password
or API token is stored in this repository.

Keep the environment approval gates enabled. See
[PyPI's Trusted Publishing guide](https://docs.pypi.org/trusted-publishers/using-a-publisher/).

## Prepare the release

1. Update the version in `package.json` and add a dated changelog entry. Python
   derives its version from `package.json`; do not edit `_version.py`.
2. Finish the README and release notes before building. PyPI's description comes
   from the packaged README. Editing the GitHub README does not update an
   already-uploaded release's description.
3. Run the native checks below, open a pull request, and merge after CI passes.

```sh
jlpm install --immutable
jlpm lint:check
jlpm test:types
jlpm build:prod
python -m build
python -m twine check --strict dist/*
```

From the merged `main` checkout, set the release variables and push the tag:

```sh
NEAT_VERSION=$(node -p 'require("./package.json").version')
NEAT_TAG="v${NEAT_VERSION}"
git tag -a "$NEAT_TAG" -m "Neat Notebook ${NEAT_VERSION}"
git push origin "$NEAT_TAG"
```

Do not move a published tag or reuse a registry version for different content.
The workflow requires the tag to match `package.json` and belong to `main`.

## Publish and verify TestPyPI

Dispatch the workflow from the repository checkout:

```sh
gh workflow run publish.yml --ref "$NEAT_TAG" -f index=testpypi
```

The workflow builds the archives and runs the compatibility tests. After they
pass, open the run, choose **Review deployments**, select **testpypi**, and choose
**Approve and deploy**.

Validate the registry installation in a disposable environment. Install the host
dependencies from PyPI first, then fetch only Neat Notebook from TestPyPI:

```sh
NEAT_TEST_HOST=$(mktemp -d)
python -m venv "$NEAT_TEST_HOST"
"$NEAT_TEST_HOST/bin/python" -m pip install \
  'notebook==7.5.6' 'jupyterlab==4.5.7'
"$NEAT_TEST_HOST/bin/python" -m pip install \
  --index-url https://test.pypi.org/simple/ --no-deps "neat-notebook==${NEAT_VERSION}"
"$NEAT_TEST_HOST/bin/python" -m pip check
"$NEAT_TEST_HOST/bin/jupyter" labextension list
```

Here `--no-deps` isolates the test index after installing the host dependencies.
It must not be used to hide dependency conflicts. Follow the installed-package
and browser checks in [CONTRIBUTING.md](CONTRIBUTING.md).

## Publish and verify PyPI

After TestPyPI verification, dispatch the production run:

```sh
gh workflow run publish.yml --ref "$NEAT_TAG" -f index=pypi
```

After its checks pass, approve the **pypi** environment deployment. Verify an
ordinary installation from PyPI in a fresh environment, run `pip check`, and
confirm discovery with `jupyter labextension list`.

Download `extension-artifacts` from that successful production workflow. Compare
the wheel and source archive's SHA-256 hashes with the PyPI release, attach those
archives to the matching GitHub release, add the changelog notes, and publish it.
Keep both registry workflows and their provenance records as release evidence.
