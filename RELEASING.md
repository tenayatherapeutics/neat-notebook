# Releasing Neat Notebook

The repository is publication-ready tooling, not permission to upload a package
automatically. Ordinary pushes, pull requests, tags, and draft GitHub releases
do **not** publish to a package registry. The `Publish` workflow is manual and
requires an approved `testpypi` or `pypi` environment deployment.

Release owner and maintainer: Farshad Farshidfar
([@farshadf](https://github.com/farshadf), farshidfar@gmail.com).

## One-time registry setup

Sign in to your own PyPI account and register a **pending Trusted Publisher** at
<https://pypi.org/manage/account/publishing/>. No API token is required or stored
in this repository. Register the following exact values:

| Field                | Production           | Test index           |
| -------------------- | -------------------- | -------------------- |
| Package/project name | `neat-notebook`      | `neat-notebook`      |
| GitHub owner         | `tenayatherapeutics` | `tenayatherapeutics` |
| Repository           | `neat-notebook`      | `neat-notebook`      |
| Workflow filename    | `publish.yml`        | `publish.yml`        |
| Environment          | `pypi`               | `testpypi`           |

TestPyPI is a separate service and account:
<https://test.pypi.org/manage/account/publishing/>. A pending publisher does not
reserve a name; check availability immediately before the first upload.
Configure both GitHub environments with `farshadf` as a required reviewer. A
human maintainer must approve each registry deployment. Do not remove the
environment gate or replace OIDC with a long-lived token to bypass setup.

References: [PyPI pending publishers](https://docs.pypi.org/trusted-publishers/creating-a-project-through-oidc/)
and [PyPA's publishing guide](https://packaging.python.org/en/latest/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/).

## Prepare a version

1. Update `package.json`'s version and `CHANGELOG.md`; Python derives its version
   from the same file. Do not hand-edit `neat_notebook/_version.py`.
2. Run CI and review compatibility results, screenshots, and known host issues.
   Build and check both archives with `python -m build` and
   `python -m twine check --strict dist/*`.
3. Merge to `main`, then create and push a matching tag such as `v0.1.4`. Do not
   reuse a tag or registry version for different content.
4. Prepare a draft GitHub release. Attach the CI-built wheel and source archive
   from that exact commit, not an unrelated local build.

The publishing workflow rejects branch refs, mismatched version tags, commits
outside this repository's `main` history, and failed CI. It reruns the reusable
CI workflow, then downloads those validated artifacts into a separate OIDC-only
publishing job. No source checkout or build runs in that publishing job.

## Upload only after approval

First dispatch the workflow on the version tag for TestPyPI:

```sh
gh workflow run publish.yml --ref v0.1.4 -f index=testpypi
```

Approve its environment deployment in GitHub Actions. Validate installation from
TestPyPI in a disposable environment, installing normal host dependencies from
PyPI separately rather than allowing a mixed-index dependency search:

```sh
python -m pip install 'notebook==7.5.6' 'jupyterlab==4.5.7'
python -m pip install --index-url https://test.pypi.org/simple/ --no-deps neat-notebook==0.1.4
python -m pip check
```

Here `--no-deps` only isolates the test index after dependencies have already
been installed and checked. It is not a workaround for an incompatible host.

After successful TestPyPI verification, dispatch for production and approve it:

```sh
gh workflow run publish.yml --ref v0.1.4 -f index=pypi
```

Verify a fresh ordinary `pip install neat-notebook==0.1.4` and `pip check`, then
publish the GitHub release and replace the README's pre-publication notice with
the released version. Keep the validated artifacts and provenance available.
Only then use the prepared [upstream follow-up](docs/UPSTREAM_FOLLOWUP.md).

An npm release and conda-forge recipe are optional later steps. Neither is
required for users to install this prebuilt Python extension.
