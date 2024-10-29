from django.apps import AppConfig
from django.core.management import call_command

class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

    def ready(self):

        on_start()

def on_start():
    # Run database migrations
    call_command('migrate')
