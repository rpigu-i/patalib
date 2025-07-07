# PataLib a Pataphysical toolkit for Python

PataLib for Python is a toolkit for implementing
pataphysically inspired algorithims.

## Outline

The full documentation and site for
PataLib can be found at:

https://rpigu-i.github.io/patalib/

This repository contains:

1.) A set of Python classes used for generating Pata-data

2.) Automated doc and fuzz tests


## Installation

### Using Poetry (Recommended)

This project now supports Poetry for dependency management and packaging. To install using Poetry:

```bash
# Install the project and its dependencies
poetry install

# Run tests with Poetry
poetry run python test/test_runner.py
```

### Using pip (Traditional)

You can still install using pip and the traditional setup.py:

```bash
pip install -e .
```

## Dependencies

Mac user will need to install Xcode first

```
xcode-select --install
```

Once installed, please install the latest version of the WordNet data:

```
python -m nltk.downloader wordnet
```

Note, you should ensure you have version 3.9.1 or higher installed, as there is a bug in version 3.9 of NLTK which prevents wordnet from loading. See: https://www.nltk.org/news.html

## Tests

All tests are written using doctest and hypothesis.

Tests can be run from the command line in several ways:

### Using Poetry
```bash
poetry run python test/test_runner.py
```

### Using traditional Python
```bash
python test/test_runner.py
```

### Direct doctest execution
```bash
python -m doctest test/test_runner.py 
```
