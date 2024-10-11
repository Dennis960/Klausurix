from dataclasses import dataclass
from models.question import Question


@dataclass
class Exam:
    title: str
    questions: list[Question]
