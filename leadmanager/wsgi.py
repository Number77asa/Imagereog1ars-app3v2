"""
WSGI config for leadmanager project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see

"""

import sys
import os

path = '/home/ubuntu/Imagereog1ars-app3v2/leadmanager'

if path not in sys.path:
    sys.path.insert(0, path)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'leadmanager.settings')

application = get_wsgi_application()
