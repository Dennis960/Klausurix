from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Question, Exam

# View for the index page (GET request)
def index(request):
    exams = Exam.objects.all()
    return render(request, 'index.html', {
        'open_exams': exams
    })

# View for the exam page (GET request)
def exam(request, exam_id):
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

def exam_questions(request, exam_id):
    if request.method == 'POST':
        # Extract the input from the form
        question_text = request.POST.get('question_text', '')  # Get the 'question_text' value from the form
        answer_text = request.POST.get('answer_text', '')  # Get the 'answer_text' value from the form
        print(f"Question text: {question_text}, Answer text: {answer_text}")
        # Create a new Question object and save it to the database
        exam = Exam.objects.get(id=exam_id)
        question = Question(question_text=question_text, answer_text=answer_text, exam=exam)
        question.save()

    return HttpResponseRedirect(reverse('exam', args=[exam_id]))

def exam_questions_id(request, exam_id, question_id):
    if request.method == 'POST':
        # Extract the input from the form
        question_text = request.POST.get('question_text', '')  # Get the 'question_text' value from the form
        answer_text = request.POST.get('answer_text', '')  # Get the 'answer_text' value from the form
        # Update the Question object with the specified ID
        question = Question.objects.get(id=question_id)
        question.question_text = question_text
        question.answer_text = answer_text
        question.save()
    elif request.method == 'DELETE':
        # Delete the Question object with the specified ID
        question = Question.objects.get(id=question_id)
        question.delete()
    
    return HttpResponseRedirect(reverse('exam', args=[exam_id]))