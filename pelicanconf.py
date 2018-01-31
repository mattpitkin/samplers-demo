#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Matthew Pitkin'
SITENAME = 'Samplers Demo'
SITESUBTITLE = u'A demonstration of Python MCMC samplers'
SITEURL = ''
PATH = 'content'
TIMEZONE = 'Europe/London'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Set the article URL
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#MARKUP = ('md', 'ipynb')
#PLUGINS = ['ipynb.markup']

MARKUP = ['md']
PLUGIN_PATHS = ['./plugins', './plugins/pelican-plugins']
PLUGINS = [
    'summary',       # auto-summarizing articles
    'feed_summary',  # use summaries for RSS, not full articles
    'ipynb.liquid',  # for embedding notebooks
    'liquid_tags.img',  # embedding images
    'liquid_tags.include_code',  # including code blocks
    'liquid_tags.literal'
]
IGNORE_FILES = ['.ipynb_checkpoints']

# for liquid tags
CODE_DIR = 'downloads/code'
NOTEBOOK_DIR = 'downloads/notebooks'

# THEME SETTINGS
THEME = './theme/'

ABOUT_PAGE = '/pages/about.html'
TWITTER_USERNAME = 'mattpitkin'
GITHUB_USERNAME = 'mattpitkin'
STACKOVERFLOW_ADDRESS = 'https://stackoverflow.com/users/1862861/matt-pitkin'
AUTHOR_WEBSITE = 'http://www.astro.gla.ac.uk/~matthew'
AUTHOR_BLOG = 'http://cosmiczoo.blogspot.com'
SHOW_ARCHIVES = False
SHOW_FEED = False  # Need to address large feeds

ENABLE_MATHJAX = True

STATIC_PATHS = ['images', 'figures', 'downloads', 'favicon.ico']

# Footer info

LICENSE_URL = "https://github.com/mattpitkin/samplers-demo/blob/master/LICENSE"
LICENSE = "MIT"
