#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://mattpitkin.github.io/samplers-demo'
RELATIVE_URLS = False

SHOW_FEED = False
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
FEED_USE_SUMMARY = False  # from the feed_summary plugin

DELETE_OUTPUT_DIRECTORY = True

DISQUS_SITENAME = "sampler-demos"
#GOOGLE_ANALYTICS = "" # add later
