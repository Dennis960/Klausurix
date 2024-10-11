from kivy.uix.boxlayout import BoxLayout
from widgets.button import KlausurixButton
from widgets.textinput import KlausurixTextInput
from widgets.question import KlausurixQuestion
from services import export
from models.exam import Exam
from models.question import Question, PictureQuestion
from kivymd.app import MDApp


class KlausurixApp(MDApp):
    exam: Exam = Exam("Example Exam", [
        Question("What is the capital of Germany?", "Berlin"),
        PictureQuestion("What is the capital of France?", "Paris",
                        "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Paris_Night.jpg/800px-Paris_Night.jpg")
    ])

    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        button = KlausurixButton(
            text="Create PDF", size_hint=(None, None), size=(200, 50))
        text_input = KlausurixTextInput(
            hint_text="Enter the target filename", multiline=False)
        for question in self.exam.questions:
            layout.add_widget(KlausurixQuestion(question))
        layout.add_widget(button)
        layout.add_widget(text_input)

        button.bind(on_press=lambda _: export.create_pdf(
            text_input.text, self.exam))

        return layout
