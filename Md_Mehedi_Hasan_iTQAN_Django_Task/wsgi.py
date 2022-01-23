"""
WSGI config for Md_Mehedi_Hasan_iTQAN_Django_Task project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Md_Mehedi_Hasan_iTQAN_Django_Task.settings')

application = get_wsgi_application()
