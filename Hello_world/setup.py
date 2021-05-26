from setuptools import setup
from Cython.Build import cythonize

setup(
	ext_models = cythonize("hello_world.pyx")
	)