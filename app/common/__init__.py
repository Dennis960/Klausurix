import random
from ..models import Question, Exam


def activate_random_number_of_questions(exam: Exam, number_of_questions: int) -> None:
    questions = Question.objects.filter(exam=exam)

    # TODO implement logic. Currently, it just inverts the is_active flag, but it should instead activate a random number of questions
    for question in questions:
        question.is_active = not question.is_active
        question.save()
        