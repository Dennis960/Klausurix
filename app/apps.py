from django.apps import AppConfig
from django.core.management import call_command
from io import StringIO

class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

    def ready(self):

        on_start()

def on_start():
    out = StringIO()
    err = StringIO()
    # Run database migrations
    call_command('migrate', interactive=False, stdout=out, stderr=err)
