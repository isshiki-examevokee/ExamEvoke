from django.db import models
from django.core.validators import MinValueValidator

from admin_panel.organizations.model import Organization
from utils.timestamp_mixin import TimestampMixin


class Exam(TimestampMixin):
    """
    Core Exam model containing only the basic exam information.
    Settings are managed at the batch level.
    """
    DIFFICULTY_CHOICES = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    ]

    OBJECTIVE_CHOICES = [
        ('Semester Exam', 'Semester Exam'),
        ('Mock Exam', 'Mock Exam'),
        ('Entrance Exam', 'Entrance Exam'),
        ('Test Series', 'Test Series'),
    ]

    # Basic Details
    name = models.CharField(
        max_length=255,
        help_text="Name of the exam"
    )
    objective = models.CharField(
        max_length=50,
        choices=OBJECTIVE_CHOICES,
        help_text="Purpose of the exam"
    )
    duration = models.DurationField(
        help_text="Duration of the exam"
    )
    difficulty = models.CharField(
        max_length=20,
        choices=DIFFICULTY_CHOICES,
        help_text="Difficulty level of the exam"
    )
    department = models.CharField(
        max_length=255,
        help_text="Department conducting the exam"
    )
    semester = models.CharField(
        max_length=50,
        help_text="Semester for which exam is being conducted"
    )
    subject = models.CharField(
        max_length=255,
        help_text="Subject of the exam"
    )
    exam_code = models.CharField(
        max_length=50,
        unique=True,
        help_text="Unique code for the exam"
    )

    # Questions and Marks
    total_questions = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        help_text="Total number of questions in the exam"
    )
    total_marks = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        help_text="Total marks for the exam"
    )

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        help_text="Organization conducting the exam"
    )

    class Meta:
        verbose_name = 'Exam'
        verbose_name_plural = 'Exams'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.exam_code}"
