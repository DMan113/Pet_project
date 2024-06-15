from django.apps import AppConfig

class TransportationConfig(AppConfig):
    name = 'transportation'

    def ready(self):
        import transportation.signals
