from django.apps import AppConfig


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'
    def ready(self):
        on_start()

def on_start():
    # TODO remove this
    try:
        from .models import Exam
        # Create dummy exams with id 1 and 2 if not already present
        if not Exam.objects.filter(id=1).exists():
            Exam.objects.create(id=1, title='Coma 1')
        if not Exam.objects.filter(id=2).exists():
            Exam.objects.create(id=2, title='Coma 2')
    except:
        pass