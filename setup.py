#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='avatar-generator',
    version='0.3',
    author="Guillaume Subiron",
    author_email="maethor+pip@subiron.org",
    description="Generates default avatars from a given string (such as username).",
    long_description=open('README.md').read(),
    packages=find_packages(),
    package_data={'': ['*.otf', 'data/*.otf']},
    include_package_data=True,
    install_requires=['pillow'],
    url='http://github.com/maethor/avatar-generator',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers"
    ],
    license="WTFPL",
)
