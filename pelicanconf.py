#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Sara Thurman'
SITENAME = u'Select * from Languages'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'


# Static paths will be copied without parsing their contents
STATIC_PATHS = ['extra','images']

# Shift the installed location of a file
EXTRA_PATH_METADATA = {
        'extra/CNAME': {'path': 'CNAME'},
        }

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/srthurman'),
          ('Twitter', 'https://twitter.com/thurmSR'),
          ('Linkedin', 'https://www.linkedin.com/in/srthurman'),)

DEFAULT_PAGINATION = 10

# Theme settings
THEME = '/home/sarat/python/pelican_themes/pelican-themes/gum'
#THEME = '/home/sarat/python/pelican_themes/pelican-elegant'


GITHUB_URL = 'https://github.com/srthurman'
TWITTER_URL = 'https://twitter.com/thurmSR'
LINKEDIN_URL = 'https://www.linkedin.com/in/srthurman'

#MD_EXTENSIONS = ['markdown.extensions.sane_lists']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
