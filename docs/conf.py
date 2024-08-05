# docs/conf.py

import os
import sys
import django

# Add the project root directory to sys.path (directory containing manage.py)
sys.path.insert(0, os.path.abspath('..'))  # Points to your project root

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'band_site'

# Initialize Django
django.setup()

# -- Project information -----------------------------------------------------
project = 'Band Site'
author = 'Your Name'
release = '1.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

# -- Options for HTML output -------------------------------------------------
html_theme = 'alabaster'
html_static_path = ['_static']

# Debugging: Verify paths
print("Python Path:", sys.path)
print("Current Working Directory:", os.getcwd())
