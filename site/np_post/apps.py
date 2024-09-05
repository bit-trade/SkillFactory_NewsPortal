from django.apps import AppConfig


class NpPostConfig(AppConfig):
    name = 'np_post'
    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):
        import np_post.signals

