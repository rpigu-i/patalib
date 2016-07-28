******************************
Patalib basic doc tests
******************************

.. contents:: Table of Contents

Introduction
************

Basic doc tests via unit test framework
for testing Patalib functionality.

All tests are written into RST files.


Importing PataLib
*****************

    >>> from patalib import Antonym, Synonym, Syzygy, Anomaly, Clinamen

Next we need to create some test data

    >>> input_word = "bye"
    >>> input_dict = ["Hello", "Hi", "Bee", "Bin"]
    >>> number_of_anom = 1
    >>> input_swerve = 1
       


Test generating a synonym list
******************************

A pataphysical synonym list can be generated as follows:

    >>> synonym_list = Synonym().generate_synonym(input_word)
 

Test generating an antonym list
*******************************

A pataphysical antonym list can be generated as follows:

    >>> antonym_list = Antonym().generate_antonym(input_word)


Test generating a syzygy list
******************************

A pataphysical syzygy list can be generated as follows:

    >>> syzygy_list = Syzygy().generate_syzygy(input_word)


Test generating an anomaly list
*******************************

A pataphysical anomaly list can be generated as follows:

    >>> anomaly_list = Anomaly().generate_anomaly(input_word, input_dict, number_of_anom)


Test generating a clinamen list
*******************************

A pataphysical clinamen list can be generated as follows:

    >>> clinamen_list = Clinamen().generate_clinamen(input_word, input_dict, input_swerve)



