# -*- coding: utf-8 -*-
import io
from setuptools import setup, find_packages

with io.open('README.md', 'rt', encoding='utf8') as f:
    readme = f.read()

setup(
    name='CRWA Flagging Website',
    version='0.1.0',
    packages=find_packages(),
    author='Code for Boston',
    maintainer='Charles River Watershed Association',
    include_package_data=True,
    tests_require=[
        'pytest',
    ],
    install_requires=[
        'pyyaml',
        'pandas', # TODO: Should this be required down the line?
        'flask'
    ],
    url='?',
    description='Flagging website for the CRWA',
    long_description=readme
)