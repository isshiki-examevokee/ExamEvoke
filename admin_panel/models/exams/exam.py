import uuid

from django.db import models


class ExamType(models.TextChoices):
    SEMESTER = "SEMESTER"


class ExamDifficulty(models.TextChoices):
    EASY = "EASY"
    MEDIUM = "MEDIUM"
    HARD = "HARD"


class Exam(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )
    name = models.CharField(blank=False, null=False, max_length=255)
    type = models.CharField(
        blank=False,
        null=False,
        max_length=255,
        choices=ExamType.choices,
        default=ExamType.SEMESTER,
    )
    duration = models.PositiveIntegerField()
    difficulty = models.CharField(
        blank=False,
        null=False,
        max_length=255,
        choices=ExamDifficulty.choices,
        default=ExamDifficulty.choices,
    )
    department = models.CharField(
        blank=True,
        null=True,
        max_length=255,
    )
    semester = models.CharField(
        blank=True,
        null=True,
        max_length=255,
    )
    subject = models.CharField(
        blank=True,
        null=True,
        max_length=255,
    )
    exam_code = models.CharField(
        blank=True,
        null=True,
        max_length=255,
    )
    total_questions = models.PositiveIntegerField(
        blank=True,
        null=True,
    )
    total_marks = models.PositiveIntegerField(
        blank=True,
        null=True,
    )
    domain = models.CharField(
        blank=True,
        null=True,
        max_length=255,
    )
    subject = models.CharField(
        blank=True,
        null=True,
        max_length=255,
    )
