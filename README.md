# PataLib a Pataphysical toolkit for Python

PataLib for Python is a toolkit for implementing
pataphysically inspired algorithims.

## Outline

The full documentation and site for
PataLib can be found at:

https://patamechanix.github.io/patalib/

This repository contains:

1.) A set of Python classes used for generating Pata-data

2.) Automated doc and fuzz tests


## Dependencies

Once installed, please install the latest version of the WordNet data:

python -m nltk.downloader wordnet


## Tests

All tests are written using doctest and hypothesis.

Tests can be run from the command line inside the test directory as follows:

> python -m doctest test_runner.py 

