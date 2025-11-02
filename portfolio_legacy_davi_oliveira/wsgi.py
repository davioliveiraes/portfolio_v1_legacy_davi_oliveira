import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_legacy_davi_oliveira.settings')

application = get_wsgi_application()
