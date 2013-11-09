#!/usr/bin/env python
import os
import sys


sys.path.append('/home/czk/djangoproject/uvideo')

os.environ['DJANGO_SETTINGS_MODULE'] = 'uvideo.settings'
#os.environ['PYTHON_EGG_CACHE'] = '/tmp/.python-eggs'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()