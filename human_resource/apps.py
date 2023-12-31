from django.apps import AppConfig


class HumanResourceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'human_resource'

    def ready(self):
        import human_resource.signals
