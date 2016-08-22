"""
WSGI config for enndc_management project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys
import site

ROOT_DIR = '/var/www/cmdb/enndc_management'
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)



sys.path.append(os.path.dirname(os.path.dirname(__file__)))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "enndc_management.settings")
os.environ['PYTHON_EGG_CACHE'] = '/tmp/.python-eggs'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
