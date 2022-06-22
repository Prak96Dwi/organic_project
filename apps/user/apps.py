""" apps/user/apps.py """
from django.apps import AppConfig


class UserConfig(AppConfig):
    """
    UserConfig class
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.user'

    def ready(self):
        import apps.user.signals
