# -*- coding: utf-8 -*-
"""Installer for the slc.zopescript package."""

from setuptools import find_packages
from setuptools import setup

import os


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = \
    read('README.rst') + \
    read('docs', 'CHANGELOG.rst') + \
    read('docs', 'LICENSE.rst')

setup(
    name='slc.zopescript',
    version='2.0.1.dev0',
    description="Base classes for running code as Zope console scripts",
    long_description=long_description,
    # Get more from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Zope2",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ],
    keywords='Zope console script',
    author='Syslab.com GmbH',
    author_email='info@syslab.com',
    url='http://pypi.python.org/pypi/slc.zopescript',
    license='BSD',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['slc'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Plone',
        'setuptools',
        'plone.api',
    ],
    extras_require={
        'test': [
            'mock',
            'unittest2',
        ],
        'develop': [
            'coverage',
            'flake8',
            'jarn.mkrelease',
            'Sphinx',
            'zest.releaser',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
