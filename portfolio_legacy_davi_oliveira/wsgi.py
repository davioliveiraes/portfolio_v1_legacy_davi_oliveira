import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "portfolio_legacy_davi_oliveira.settings"
)

application = get_wsgi_application()

from whitenoise import WhiteNoise
from django.conf import settings

application = WhiteNoise(application)
application.add_files(settings.MEDIA_ROOT, prefix="media/")
