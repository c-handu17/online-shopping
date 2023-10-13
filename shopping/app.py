from django.apps import AppConfig


class ShoppingAppConfig(AppConfig):
    name = "shopping"

    def ready(self):
        from shopping import signals # pylint: disable=unused-variable
