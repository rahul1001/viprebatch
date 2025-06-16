# conf.py

import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# Project information
project = 'viprebatch'
author = 'installusingprokey'

# Extensions
extensions = ['myst_parser']

# Source suffix
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# The master toctree document.
master_doc = 'index'

# HTML theme
html_theme = 'alabaster'
