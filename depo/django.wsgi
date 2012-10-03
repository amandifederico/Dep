import os
import sys

sys.path.append('/var/www/depo')
os.environ['DJANGO_SETTINGS_MODULE'] = 'depo.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
