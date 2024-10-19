###############################################################################
# Auto-generated by `jupyter-book config`
# If you wish to continue using _config.yml, make edits to that file and
# re-generate this one.
###############################################################################
import os 
import sys

sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('../../'))

project = 'openaicg2'
author = 'Lujun Zou'
copyright = '2024 Lujun Zou, Wenfei Li'
release = '0.1'

bibtex_bibfiles = ['references.bib']
comments_config = {'hypothesis': False, 'utterances': False}
exclude_patterns = ['**.ipynb_checkpoints', '.DS_Store', 'Thumbs.db', '_build']
extensions = ['sphinx.ext.viewcode','sphinx.ext.napoleon','sphinx_togglebutton', 'sphinx_copybutton', 'sphinx_thebe', 'sphinx_comments', 'sphinx.ext.intersphinx', 'sphinx_design', 'sphinx_book_theme', 'sphinx.ext.autodoc','sphinxcontrib.bibtex', 'sphinx.ext.napoleon']

# The master toctree document
master_doc = 'index'

html_baseurl = ''
html_favicon = ''
html_logo = 'logo.png'
html_sourcelink_suffix = ''
html_theme = 'sphinx_book_theme'
html_theme_options = {'search_bar_text': 'Search this book...', 'launch_buttons': {'notebook_interface': 'classic', 'binderhub_url': '', 'jupyterhub_url': '', 'thebe': False, 'colab_url': ''}, 'path_to_docs': 'docs', 'repository_url': ' https://github.com/LiGroup-NJUBiophysics/openAICG2', 'repository_branch': 'main', 'extra_footer': '',  'announcement': '', 'analytics': {'google_analytics_id': ''}, 'use_repository_button': True, 'use_edit_page_button': False, 'use_issues_button': False}
html_title = 'OpenAICG2'
latex_engine = 'pdflatex'
myst_enable_extensions = ['colon_fence', 'dollarmath', 'linkify', 'substitution', 'tasklist']
myst_url_schemes = ['mailto', 'http', 'https']
nb_execution_allow_errors = False
nb_execution_cache_path = ''
nb_execution_excludepatterns = []
nb_execution_in_temp = False
nb_execution_mode = 'off'
nb_execution_timeout = 30
nb_output_stderr = 'show'
numfig = True
pygments_style = 'sphinx'
suppress_warnings = ['myst.domains']
use_jupyterbook_latex = True
