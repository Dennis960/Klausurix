from dataclasses import dataclass


@dataclass
class Question:
    text: str
    answer: str


@dataclass
class PictureQuestion(Question):
    picture_base64: str  # To be determined how to store and retreive images
