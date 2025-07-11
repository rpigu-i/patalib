# PyPI Publishing Workflow

This repository includes a GitHub Actions workflow for automatically publishing the `patalib` package to PyPI when new version tags are pushed.

## How it works

The workflow is triggered when you push a tag that starts with `v` (e.g., `v2.1.0`, `v2.2.0`).

### Workflow Steps

1. **Testing**: Runs tests across multiple Python versions (3.8 through 3.12) to ensure compatibility
2. **Building**: Creates both source distribution (`.tar.gz`) and wheel (`.whl`) packages
3. **Publishing**: 
   - Pre-release versions (containing `rc`, `alpha`, or `beta`) are published to Test PyPI
   - Stable releases are published to the main PyPI

## Publishing a new version

To publish a new version:

1. Update the version number in both:
   - `pyproject.toml` (line 7)
   - `setup.py` (line 6)

2. Commit the changes:
   ```bash
   git add pyproject.toml setup.py
   git commit -m "Bump version to X.Y.Z"
   ```

3. Create and push a version tag:
   ```bash
   git tag vX.Y.Z
   git push origin vX.Y.Z
   ```

4. The GitHub Actions workflow will automatically:
   - Run tests
   - Build the package
   - Publish to PyPI

## Prerequisites

Before the first publication, you need to set up PyPI trusted publishing, the example below demonstrates how this works:

1. Go to your [PyPI account settings](https://pypi.org/manage/account/publishing/)
2. Add a new trusted publisher with these settings:
   - **Owner**: `<name>`
   - **Repository name**: `patalib`
   - **Workflow name**: `publish-to-pypi.yml`
   - **Environment name**: (leave empty)

This allows GitHub Actions to publish to PyPI without storing API tokens as secrets.

## Testing releases

For testing purposes, you can create pre-release tags:
- `v2.1.0-rc1` (release candidate)
- `v2.1.0-alpha1` (alpha release)  
- `v2.1.0-beta1` (beta release)

These will be published to [Test PyPI](https://test.pypi.org/) instead of the main PyPI.

## Manual publishing

If you need to publish manually:

```bash
# Install build tools
pip install build twine

# Build the package
python setup.py sdist bdist_wheel

# Upload to PyPI (requires API token)
twine upload dist/*
```
