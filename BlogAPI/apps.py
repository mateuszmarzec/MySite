from django.apps import AppConfig


class BlogapiConfig(AppConfig):
    name = 'BlogAPI'

    def ready(self):
        import BlogAPI.signals