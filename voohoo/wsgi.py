"""
WSGI config for voohoo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os,sys
from django.core.wsgi import get_wsgi_application

curr_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(curr_dir)

if parent_dir not in sys.path:
    sys.path.append(parent_dir)

#sys.path.append(curr_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'voohoo.settings'

application = get_wsgi_application()