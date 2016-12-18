from django.apps import AppConfig

class VaasConfig(AppConfig):
    name = 'vaas'

    def ready(self):
        import vaas.manager.signals