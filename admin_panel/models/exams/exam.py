import uuid

from django.db import models

from admin_panel.models.university.organization import Organization


class ExamType(models.TextChoices):
    SEMESTER = "SEMESTER"


class ExamDifficulty(models.TextChoices):
    EASY = "EASY"
    MEDIUM = "MEDIUM"
    HARD = "HARD"


class ExamModeChoices(models.TextChoices):
    CENTER_BASED_TEST = "CENTER_BASED_TEST"


class ExamConfiguration(models.Model):
    MODE_CHOICES = [
        ('center_based', 'Center Based Test'),
        ('home_based', 'Home Based Test'),
    ]
    
    mode = models.CharField(
        max_length=50,
        choices=ExamModeChoices.choices,
        default=ExamModeChoices.CENTER_BASED_TEST
    )
    start_date = models.DateField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    show_scientific_calculator = models.BooleanField(default=False)
    activity_log = models.BooleanField(default=False)
    is_submit_enable = models.BooleanField(default=False)
    lock_screen = models.BooleanField(default=False)
    maximum_question_attempt = models.IntegerField(null=True, blank=True)
    test_download_password = models.CharField(max_length=100, blank=True)
    essay_question_time_limit = models.TimeField(null=True, blank=True)
    minimum_question_time = models.TimeField(null=True, blank=True)
    late_login_time = models.IntegerField(null=True, blank=True)
    
    mandatory_attempt_all_questions = models.BooleanField(default=False)
    essay_question_time_limit_enable = models.BooleanField(default=False)
    enable_backward_forward_movement = models.BooleanField(default=False)
    
    overall_selection_criteria_1 = models.IntegerField(default=95)
    overall_selection_criteria_2 = models.IntegerField(default=95)
    
    section_instructions = models.BooleanField(default=False)
    topic_attempt_limits = models.BooleanField(default=False)
    section_wise_break = models.BooleanField(default=False)


class Exam(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )
    name = models.CharField(blank=False, null=False, max_length=255)
    organization = models.ForeignKey(
        Organization,
        related_name="exams",
        on_delete=models.CASCADE
    )
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
    config = models.ForeignKey(
        ExamConfiguration,
        related_name="exams",
        on_delete=models.CASCADE,
    )
