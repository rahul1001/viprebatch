# conf.py

import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# Project information
project = 'viprebatch'
author = 'installusingprokey'

# -- General configuration ---------------------------------------------------

extensions = [
    'myst_parser',  # to support Markdown files
]

# Source file suffixes - support both reStructuredText and Markdown
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

master_doc = 'index'  # your root document

templates_path = ['_templates']  # Important: enables your custom templates

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

html_theme = 'alabaster'

# You can still add html_meta here if you want, but with the new Read the Docs addons
# custom template is the reliable way to inject meta tags.

# If you want to add other meta tags, do so in your _templates/layout.html

html_meta = {
    "msvalidate.01": "C49E36B78750F57FF10DE13279028CBC",
}

# Path to static files
html_static_path = ['_static']

# Path to logo file
html_logo = '_static/logo.jpg'
