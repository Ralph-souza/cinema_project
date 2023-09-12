from django.apps import AppConfig


class SalesAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.sales_app'


class CoreConfig(AppConfig):
    name = 'apps.sales_app'
