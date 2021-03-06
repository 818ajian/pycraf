#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
The atm subpackage provides an implementation of the atmospheric models of
`ITU-R Rec. P.676-10 <https://www.itu.int/rec/R-REC-P.676-10-201309-S/en>`_.
For this, various other algorithms from the following two ITU-R
Recommendations are
necessary:

    - `ITU-R Rec. P.835-5 <https://www.itu.int/rec/R-REC-P.835-5-201202-I/en>`_,
      which contains the Standard and several special atmospheric profiles.
    - `ITU-R Rec. P.453-12 <https://www.itu.int/rec/R-REC-P.453-12-201609-I/en>`_,
      which is used to calculate the refractive index from temperature and
      water/total air pressure. Furthermore, P.453 has formulae to derive the
      saturation water pressure from temperature and total air pressure,
      as well as the water pressure from temperature, pressure and humidity, or
      alternatively from temperature and wator vapor density.

Notes
-----
A new version of ITU-R P.676 is available,
`ITU-R Rec. P.676-11 <https://www.itu.int/rec/R-REC-P.676-11-201609-I/en>`_,
which has a modified algorithm for Annex 2. We will implement this soon.
'''

from .atm import *
