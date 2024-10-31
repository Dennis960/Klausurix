from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from .models import Question, Exam
import random
from .common import activate_random_number_of_questions

# View for the index page (GET request)
def index(request):
    exams = Exam.objects.all()
    return render(request, 'index.html', {
        'open_exams': exams
    })

def exams(request):
    if request.method == 'POST':
        exam = Exam(title='New Exam')
        exam.save()
        response = HttpResponse()
        response['HX-Redirect'] = reverse('exams_id', args=(exam.id,))
        return response
    if request.method == 'DELETE':
        exam = Exam.objects.get(id=request.POST.get('exam_id', ''))
        exam.delete()
        return HttpResponse()

# View for the exam page (GET request)
def exams_id(request, exam_id):
    if request.method == 'GET':
        def get_questions_for_exam(id: int):
            exam = Exam.objects.get(id=id)
            questions = Question.objects.filter(exam=exam)
            return questions
        questions = get_questions_for_exam(exam_id)
        exams = Exam.objects.all()

        return render(request, 'index.html', {
            'questions': questions,
            'exam_id': exam_id,
            'open_exams': exams
        })
    if request.method == 'DELETE':
        exam = Exam.objects.get(id=exam_id)
        exam.delete()
        response = HttpResponse()
        response['HX-Redirect'] = reverse('index')
        return response

def exam_questions(request, exam_id):
    if request.method == 'POST':
        exam = Exam.objects.get(id=exam_id)
        question = Question(exam=exam)
        question.save()
        return render(request, 'includes/question/question_form.html', {
            'exam_id': exam_id,
            'question': question
        })

def exam_questions_id(request, exam_id, question_id):
    if request.method == 'POST':
        # Extract the input from the form
        question_text = request.POST.get('question_text', '')  # Get the 'question_text' value from the form
        answer_text = request.POST.get('answer_text', '')  # Get the 'answer_text' value from the form
        is_active = request.POST.get('is_active', '') == 'on'  # Get the 'is_active' value from the form
        # Update the Question object with the specified ID
        question = Question.objects.get(id=question_id)
        question.question_text = question_text
        question.answer_text = answer_text
        question.is_active = is_active
        question.save()
        return render(request, 'includes/question/question_form.html', {
            'question': question,
            'exam_id': exam_id
        })
    elif request.method == 'DELETE':
        # Delete the Question object with the specified ID
        question = Question.objects.get(id=question_id)
        question.delete()
        return HttpResponse()

def exams_id_settings_number_of_questions(request, exam_id):
    if request.method == 'POST':
        exam = Exam.objects.get(id=exam_id)
        number_of_questions = request.POST.get('number_of_questions', 0)
        try:
            number_of_questions = int(number_of_questions)
        except ValueError:
            number_of_questions = 0
        number_of_questions = min(number_of_questions, Question.objects.filter(exam=exam).count())
        questions = Question.objects.filter(exam=exam)
        
        activate_random_number_of_questions(exam, number_of_questions)

        response = HttpResponse()
        response['HX-Redirect'] = reverse('exams_id', args=(exam.id,))
        return response