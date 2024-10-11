from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from models.question import Question


class KlausurixQuestion(MDBoxLayout):
    def __init__(self, question: Question, **kwargs):
        super(KlausurixQuestion, self).__init__(**kwargs)

        self.orientation = 'vertical'

        question_title = MDLabel(text=question.text)
        self.add_widget(question_title)

        question_answer = MDLabel(text=question.answer)
        self.add_widget(question_answer)
