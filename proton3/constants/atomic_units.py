"""Atomic units constants used in proton3.

Atomic Units are a system of units where an electron rest mass, the
elementary charge, the reduced Planck's constant and the Coulomb force constant
are all equal to 1.

This variables follow the constants defined by qmsolve at
qmsolve/util/constants.py. The change of variable naming is useful in terms of
code readability. The following conversion is made between proton3 and qmsolve:

AMSTRONG = Å
ELECTRONVOLT = eV
FEMTOSECOND = fs = femtoseconds

For more information see:
https://chem.libretexts.org/Courses/Pacific_Union_College/Quantum_Chemistry/08%3A_Multielectron_Atoms/8.01%3A_Atomic_and_Molecular_Calculations_are_Expressed_in_Atomic_Units
"""

ELECTRON_MASS = 1.0
ELEMENTARY_CHARGE = 1.0
REDUCED_PLANCK = 1.0
COULOMB_FORCE = 1.0

ANGSTROM =  1.8897261246257702
ELECTRONVOLT = 0.03674932217565499
FEMTOSECOND = 4.134137333518212 * 10.
