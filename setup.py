#!/usr/bin/env python
#:coding=utf-8:

import sys

if sys.version < '2.4':
    sys.exit('Error: Python-2.4 or newer is required. Current version:\n %s' % sys.version)

from setuptools import setup, find_packages

VERSION = "0.1"
DESCRIPTION = "Disqus API Client"
LONG_DESCRIPTION = "A Disqus (http://www.disqus.com/) API client written in python."

CLASSIFIERS = filter(None, map(str.strip,
"""                 
Intended Audience :: Developers
License :: OSI Approved :: MIT License
Programming Language :: Python
Topic :: Internet :: WWW/HTTP
""".splitlines()))

setup(name='disqus-api-client',
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      author='Ian Lewis',
      author_email='IanLewis@member.fsf.org',
      url='http://code.google.com/p/disqus-python-client/',
      license="MIT License",
      platforms=["any"],
      packages=find_packages(),
      #test_suite="disqus.tests",
      zip_safe=True
     )
