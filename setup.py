#!/usr/bin/env python
#:coding=utf-8:

from ez_setup import use_setuptools
import sys
if 'cygwin' in sys.platform.lower():
   min_version='0.6c6'
else:
   min_version='0.6a9'
try:
    use_setuptools(min_version=min_version)
except TypeError:
    # If a non-local ez_setup is already imported, it won't be able to
    # use the min_version kwarg and will bail with TypeError
    use_setuptools()

if sys.version < '2.4':
    sys.exit('Error: Python-2.4 or newer is required. Current version:\n %s' % sys.version)

from setuptools import setup, find_packages

VERSION = "0.1"
DESCRIPTION = "Disqus API Client"
LONG_DESCRIPTION = """
disqus-api-client is a full featured 
"""

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
      packages=find_packages(exclude=['ez_setup']),
      #test_suite="disqus.tests",
      zip_safe=True
     )
