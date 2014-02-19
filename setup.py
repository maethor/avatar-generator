#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from setuptools import setup, find_packages
 
import avatar_generator
 
setup(
    name='avatar_generator',
    version=avatar_generator.__version__,
    packages=find_packages(),
    author="Guillaume Subiron",
    author_email="maethor+pip@subiron.org",
    description="Generates default avatars from a given string (such as username).",
    long_description=open('README.md').read(),
    install_requires=['pillow'],
    include_package_data=True,
    url='http://github.com/maethor/avatar-generator',
    classifiers=[
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers"
    ],
    license="WTFPL",
)