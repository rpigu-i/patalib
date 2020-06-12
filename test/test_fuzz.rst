********************
PataLib Fuzz testing
********************

.. contents:: Table of Contents

Introduction
************

The following tests use the Python Fuzz testing 
library called Hypothesis.

This can be found at:

https://hypothesis.readthedocs.io/en/latest/index.html



Importing libraries
*******************

    >>> from patalib import Antonym, Synonym, Syzygy, Anomaly, Clinamen
    >>> from hypothesis import given, example
    >>> import hypothesis.strategies as st   


Test generating a synonym list
******************************

A pataphysical synonym list can be generated as follows:

    >>> @given(x=st.text())
    ... def test_synonym_vals(x): 
    ...     synonym_list = Synonym().generate_synonym(x)
 
    >>> test_synonym_vals()


Test generating an antonym list
*******************************

A pataphysical antonym list can be generated as follows:

    >>> @given(x=st.text())
    ... def test_antonym_vals(x): 
    ...     antonym_list = Antonym().generate_antonym(x)
 
    >>> test_antonym_vals()


Test generating an syzygy list
*******************************

A pataphysical syzygy list can be generated as follows:

    >>> @given(x=st.text())
    ... def test_syzygy_vals(x): 
    ...     syzygy_list = Syzygy().generate_syzygy(x)
 
    >>> test_syzygy_vals()

