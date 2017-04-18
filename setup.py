"""A setuptools based setup module for py2fa"""
import sys
# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

# Check Dependencies:
try:
    import gi
    gi.require_version('Gtk', '3.0')
    from gi.repository import Gtk, Gdk, GObject
except ImportError as e:
    print("PyGTK (version 3.0) should be installed. Install from: http://www.pygtk.org/downloads.html")
    sys.exit(1)


here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='py2fa',
    version='0.1',
    description="Two-Factor Authentication using Python and GTK",
    long_description=long_description,
    url='https://github.com/cpiehl/py2fa',
    py_modules=['main'],

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'Environment :: X11 Applications :: GTK',
        'Framework :: Flask',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
    ],
    keywords='gtk mfa security',
    entry_points={
        'console_scripts': [
            'py2fa=main:main',
        ],
    },
)
