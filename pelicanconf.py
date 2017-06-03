#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Guy Nadav'
SITENAME = "Guy Nadav's Blog"
SITEURL = ''

#THEME = "/media/ubuntu/ULTRA-FIT/Dropbox/Blog/jupyter-blog/pelican-themes/mnmlist"
#THEME = "pelican-themes/mnmlist"
#THEME = "pelican-themes/genus"
THEME = "pelican-themes/clean-blog"

SOCIAL = (('github', 'https://github.com/guyov1'),
          ('linkedin','https://www.linkedin.com/in/guynadav/'),
          ('envelope','mailto:guyov1@gmail.com'))
SHOW_SOCIAL_ON_INDEX_PAGE_HEADER = False

PATH = 'content'
STATIC_PATHS = ['images']

TIMEZONE = 'Asia/Jerusalem'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

IGNORE_FILES = ['.ipynb_checkpoints']

MARKUP = ('md', 'ipynb')
#PLUGIN_PATH = './plugins'
#PLUGINS = ['ipynb.markup']
PLUGIN_PATHS = ['./pelican-plugins', './plugins']
PLUGINS = ['ipynb.markup', 'pelican_comment_system']
PELICAN_COMMENT_SYSTEM = True

