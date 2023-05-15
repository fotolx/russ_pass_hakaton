from django.apps import AppConfig


class AdsForSaleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ads_for_sale'

    def ready(self):
        import ads_for_sale.signals