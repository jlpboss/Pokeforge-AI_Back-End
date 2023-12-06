from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("pokeforge/utils/calc_battle_cython/cython_battle.pyx"),
)