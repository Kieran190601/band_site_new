import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

# Project information
project = 'Your Project Name'
author = 'Your Name'
release = '0.1'

# Add any Sphinx extension module names here, as strings.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and directories to ignore.
exclude_patterns = []

# The theme to use for HTML and HTML Help pages.
html_theme = 'alabaster'

# Paths for static files, such as CSS.
html_static_path = ['_static']

