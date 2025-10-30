import os

from django.core.asgi import get_asgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "portfolio_legacy_davi_oliveira.settings"
)

application = get_asgi_application()
