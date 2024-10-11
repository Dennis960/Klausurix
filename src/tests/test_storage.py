import unittest
from services.storage import store_exam, load_exam
from models.exam import Exam


class StorageTestCase(unittest.TestCase):
    def test_store_and_load_exam(self):
        example_exam = Exam(
            "Example Exam", ["Question 1", "Question 2", "Question 3"])
        store_exam("example_exam", example_exam)
        loaded_exam = load_exam("example_exam")
        self.assertEqual(loaded_exam.title, example_exam.title)
        self.assertEqual(loaded_exam.questions, example_exam.questions)
