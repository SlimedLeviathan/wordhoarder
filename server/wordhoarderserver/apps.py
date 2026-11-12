from django.apps import AppConfig

class ServerConfig(AppConfig):
    name = "wordhoarderserver"

    def ready(self):
        # do stuff on startup if needed
        pass