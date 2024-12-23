#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import warnings

warnings.filterwarnings("ignore")

# -- Project information -----------------------------------------------------

project = "program_guide_EOS"
copyright = "2024, Blake Dyer"
author = "Blake Dyer"

# The short X.Y version
version = ""
# The full version, including alpha/beta/rc tags
release = "0.0.1"


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "matplotlib.sphinxext.plot_directive",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.viewcode",
    "sphinx.ext.coverage",
    "sphinx.ext.mathjax",
    "sphinx_inline_tabs",
    "sphinx.ext.todo",
    "sphinx.ext.intersphinx",
    "numpydoc",
    "IPython.sphinxext.ipython_console_highlighting",
    "IPython.sphinxext.ipython_directive",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.napoleon",
    "myst_nb",
    "sphinx_design",
    "sphinx.ext.githubpages",
]

numpydoc_show_class_members = False
nb_execution_mode = "off"
panels_add_bootstrap_css = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]
nb_execution_timeout = -1
# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# ...
# Configuration of sphinx.ext.coverage
# coverage_show_missing_items = True

# The master toctree document.
master_doc = "index"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "**.ipynb_checkpoints",
    ".asv",
    ".pytest_cache",
    "*.ipynb",
    "**deprecated**",
    "**conda_env**",
]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "friendly"

# intersphinx configuration to ease linking arviz docs
intersphinx_mapping = {
    "arviz": ("https://python.arviz.org/en/latest/", None),
    "aesara": ("https://aesara.readthedocs.io/en/latest/", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "pymc": ("https://www.pymc.io/projects/docs/en/stable/", None),
    "jax": ("https://jax.readthedocs.io/en/latest/", None),
}
# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

html_theme = "pydata_sphinx_theme"
html_theme_options = {
    "github_url": "https://github.com/numpy/numpydoc",
    "show_prev_next": False,
    "navbar_end": ["search-field.html", "navbar-icon-links.html"],
}


html_title = "%s v%s Manual" % (project, version)
html_last_updated_fmt = "%b %d, %Y"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []  # ['_static']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/blakedyer/program_guide",
            "icon": "fab fa-github-square",
        },
        {
            "name": "Twitter",
            "url": "https://twitter.com/uvicseos",
            "icon": "fab fa-twitter-square",
        },
    ],
    "show_prev_next": False,
    "navbar_start": ["navbar-logo"],
    "navbar_end": ["search-field.html", "navbar-icon-links.html"],
    "search_bar_text": "Search...",
    # "use_edit_page_button": False,  # TODO: see how to skip of fix for generated pages
    # "google_analytics_id": "UA-176578023-1",
}
html_context = {
    "github_user": "blakedyer",
    "github_repo": "program_guide_EOS",
    "github_version": "main",
    # "doc_path": "docs/source/",
}

html_sidebars = {
    "**": ["sidebar-nav-bs.html"],
}

html_title = f"{project} v{release} Manual"
html_last_updated_fmt = "%b %d, %Y"
todo_include_todos = True

autosummary_generate = True  # Turn on sphinx.ext.autosummary
autodoc_member_order = "bysource"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
# html_static_path = []

# html_css_files = [
#     "style.css",
# ]

# html_logo = "lig_sea_level.svg"

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {"learn": [], "**": ["sidebar-nav-bs.html", "sidebar-ethical-ads.html"]}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "program_guide_EOSdoc"


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,
        "program_guide_EOS.tex",
        "program\\_guide\\_EOS Documentation",
        "Blake Dyer",
        "manual",
    ),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "program_guide_EOS", "program_guide_EOS Documentation", [author], 1)]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "program_guide_EOS",
        "program_guide_EOS Documentation",
        author,
        "program_guide_EOS",
        "One line description of project.",
        "Miscellaneous",
    ),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ["search.html"]


# -- Extension configuration -------------------------------------------------
