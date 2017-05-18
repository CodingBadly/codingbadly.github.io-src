#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Seyoung Jeong'
SITENAME = u'Coding Badly'
SITEURL = 'http://codingbadly.github.io'
#SITEURL = 'http://localhost:8000/'
DISPLAY_PAGES_ON_MENU = True

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('LinkedIn', 'https://www.linkedin.com/in/seyoung/'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#THEME = '../nice-blog'
#SIDEBAR_DISPLAY = ['about', 'categories', 'tags', 'archieves']
#SIDEBAR_ABOUT = "Lo"
#THEME = 'simple'
THEME = '../pelican-themes/elegant'
PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = [ "sitemap", "plantuml" ]