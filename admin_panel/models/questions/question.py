import uuid

from django.db import models

from admin_panel.models.university.subject import Subject
from admin_panel.models.university.topic import Topic


class QuestionType(models.Choices):
    SINGLE_CHOICE = "SINGLE_CHOICE"
    MULTIPLE_CHOICE = "MULTIPLE_CHOICE"
    BLANKS = "BLANKS"
    TRUE_OR_FALSE = "TRUE_OR_FALSE"
    SINGLE_DIGIT = "SINGLE_DIGIT"
    RANGE = "RANGE"


class LanguageType(models.Choices):
    ENGLISH = "ENGLISH"
    REGIONAL = "REGIONAL"


class DifficultyType(models.Choices):
    EASY = "EASY"
    MEDIUM = "MEDIUM"
    HARD = "HARD"


class Question(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )
    text = models.TextField()
    subject = models.ForeignKey(
        Subject,
        related_name="questions",
        on_delete=models.CASCADE,
    )
    topic = models.ForeignKey(
        Topic,
        related_name="questions",
        on_delete=models.CASCADE,
    )
    type = models.CharField(choices=QuestionType.choices, max_length=255)
    language = models.CharField(choices=LanguageType.choices, max_length=255)
    difficulty = models.CharField(
        choices=DifficultyType.choices,
        max_length=255
    )
    solution = models.TextField(null=True, blank=True)
    options = models.JSONField(null=False, blank=False)
    answer = models.JSONField(null=True, blank=True)
