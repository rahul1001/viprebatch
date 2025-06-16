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

# Meta tags to include in <head>
html_meta = {
    "description": "Easy step by step instructions to install vipre using product key for new users that recently purchased the security for device protection.",
    "msvalidate.01": "C49E36B78750F57FF10DE13279028CBC"
}
