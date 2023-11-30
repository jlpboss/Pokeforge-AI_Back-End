from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("cbattletest1.pyx"),
)
