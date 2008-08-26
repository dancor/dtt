#!/usr/bin/env python
from setuptools import setup
from subprocess import Popen
import sys

setup(
    name='dtt',
    version='0.2',
    description='dynamic typing tutor',
    author='dan corson',
    author_email='danl@alum.mit.edu',
    # fixme to more specific
    url='http://dzl.no-ip.org',
    package_dir={'dtt': 'src'},
    scripts=['src/dtt', 'src/bkrd'],
    # fixme sure i'm missing some
    install_requires=['simplejson'],
)
