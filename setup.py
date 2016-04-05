# -*- coding: utf-8 -*-
"""Setup file for the NagiBack project.
"""
from __future__ import unicode_literals

import codecs
import os.path
import re
from setuptools import setup, find_packages

version = None
for line in codecs.open(os.path.join('nagiback', '__init__.py'), 'r', encoding='utf-8'):
    matcher = re.match(r"""^__version__\s*=\s*['"](.*)['"]\s*$""", line)
    version = version or matcher and matcher.group(1)

# get README content from README.md file
with codecs.open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf-8') as fd:
    long_description = fd.read()

entry_points = {'console_scripts': ['nagiback = nagiback.cli:main']}

setup(
    name='nagiback',
    version=version,
    description='No description yet.',
    long_description=long_description,
    author='mgallet',
    author_email='mgallet@19pouces.net',
    license='CeCILL-B',
    url='',
    entry_points=entry_points,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    test_suite='nagiback.tests',
    install_requires=[],
    setup_requires=[],
    classifiers=['Development Status :: 3 - Alpha', 'Operating System :: MacOS :: MacOS X',
                 'Operating System :: Microsoft :: Windows', 'Operating System :: POSIX :: BSD',
                 'Operating System :: POSIX :: Linux', 'Operating System :: Unix',
                 'License :: OSI Approved :: CEA CNRS Inria Logiciel Libre License, version 2.1 (CeCILL-2.1)',
                 'Programming Language :: Python :: 2.7', 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: 3.5'],
)