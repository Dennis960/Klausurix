from django.db import models

class Exam(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)

class Question(models.Model):
    id = models.AutoField(primary_key=True)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question_text = models.TextField()
    answer_text = models.TextField()
