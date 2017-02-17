import os
from setuptools import setup, Extension

setup(
        name='finance_formulas',
        version='0.0.1.dev0',
        ext_modules=[
            Extension('finance_formulas',
                ['finance_formulas.cpp'],
                libraries=['boost_python', 'python2.7'],
                extra_compile_args = ['-std=c++11']
                ),
            ],
        )
