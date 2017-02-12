import os
from setuptools import setup, Extension

setup(
        name='finance_formulas',
        version='0.0.1',
        ext_modules=[
            Extension('finance_formulas',
                ['finance_formulas.cpp'],
                libraries=['boost_python', 'python2.7'],
                )
            ],
        )
