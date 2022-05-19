from django.apps import AppConfig
import os
from django.conf import settings


class RawMaterialConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'static'
    path = os.path.join(settings.BASE_DIR, 'static')
