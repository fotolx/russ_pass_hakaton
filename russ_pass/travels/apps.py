from django.apps import AppConfig


class AdsForSaleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'travels'

    def ready(self):
        import travels.signals