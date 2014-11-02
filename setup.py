#!/usr/bin/env python
# encoding: utf-8
from setuptools import setup
import os
import sys

setup(
  name="metallyricsfinder",
  version="0.1",
  url="https://github.com/renatolmorais/metallyricsfinder",
  license="3-BSD",
  description="Command line tool to find lyrics for heavy metal songs",
  author="Renato Lopes de Morais",
  author_email="renatolmorais@gmail.com",
  long_description=open('README').read(),
  #packages=['metallyricsfinder'],
  #scripts=['script/alfredo'],
  classifiers = [
    "License :: OSI Approved :: BSD",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    ])

