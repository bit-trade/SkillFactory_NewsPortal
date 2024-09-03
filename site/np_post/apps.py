from django.apps import AppConfig


class NpPostConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'np_post'

    def ready(self):
        import np_post.signals

