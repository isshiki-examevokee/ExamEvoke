from django.db import models
import uuid
from utils.timestamp_mixin import TimestampMixin


class ExamMode(models.TextChoices):
    CENTER_BASED = "CENTER_BASED", "Center Based Test"
    INTERNET_BASED = "INTERNET_BASED", "Internet Based Test"
    INTERNET_BASED_HYBRID = "INTERNET_BASED_HYBRID", "Internet Based Test (Hybrid)"
    PAPER_BASED_OSM = "PAPER_BASED_OSM", "Paper Based Test (OSM)"
    PAPER_BASED_OMR = "PAPER_BASED_OMR", "Paper Based Test (OMR)"
    PAPER_BASED_ATTACHMENT = "PAPER_BASED_ATTACHMENT", "Paper Based Test (Attachment Type)"


class AuthenticationType(models.TextChoices):
    AADHAR = "AADHAR", "Aadhar Card"
    PAN = "PAN", "PAN Card"
    VOTER_ID = "VOTER_ID", "Voter ID"
    DRIVING_LICENSE = "DRIVING_LICENSE", "Driving License"


class CriteriaType(models.TextChoices):
    OVERALL = "OVERALL", "Overall"
    SECTION = "SECTION", "Section"
    SUBJECT = "SUBJECT", "Subject"


class ComparisonOperator(models.TextChoices):
    LESS_THAN = "LT", "<"
    LESS_THAN_EQUAL = "LTE", "<="
    GREATER_THAN = "GT", ">"
    GREATER_THAN_EQUAL = "GTE", ">="
    EQUAL = "EQ", "="


class LogicalOperator(models.TextChoices):
    AND = "AND", "AND"
    OR = "OR", "OR"


class ExamBatch(TimestampMixin):
    """
    Core ExamBatch model with relationships and basic fields
    """
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )
    exam = models.ForeignKey(
        'Exam',
        on_delete=models.CASCADE,
        related_name='exam_batches'
    )
    batch = models.ForeignKey(
        'Batch',
        on_delete=models.CASCADE,
        related_name='exam_batches'
    )
    organization = models.ForeignKey(
        'Organization',
        on_delete=models.CASCADE,
        related_name='exam_batches'
    )
    mode = models.CharField(
        max_length=50,
        choices=ExamMode.choices,
        help_text="Type of examination mode"
    )
    # Basic schedule
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    # Evaluation schedule
    evaluation_start_date = models.DateField(null=True, blank=True)
    evaluation_end_date = models.DateField(null=True, blank=True)
    evaluation_start_time = models.TimeField(null=True, blank=True)
    evaluation_end_time = models.TimeField(null=True, blank=True)

    class Meta:
        unique_together = ['exam', 'batch']
        ordering = ['-created_at']
        
    def __str__(self):
        return f"{self.exam.name} - {self.batch.name}"


class ExamBatchSettings(TimestampMixin):
    """
    Common settings that apply to all exam types
    """
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )
    exam_batch = models.OneToOneField(
        ExamBatch,
        on_delete=models.CASCADE,
        related_name='settings'
    )
    # Common settings
    show_scientific_calculator = models.BooleanField(default=False)
    activity_log = models.BooleanField(default=False)
    is_submit_enable = models.BooleanField(default=True)
    lock_screen = models.BooleanField(default=False)
    maximum_question_attempt = models.PositiveIntegerField(null=True, blank=True)
    test_download_password = models.CharField(max_length=255, null=True, blank=True)
    
    # Time related settings
    essay_question_time_limit = models.DurationField(null=True, blank=True)
    minimum_question_time = models.DurationField(null=True, blank=True)
    late_login_time = models.IntegerField(
        help_text="Late login time in minutes",
        null=True,
        blank=True
    )

    # Common flags
    mandatory_attempt_all = models.BooleanField(default=False)
    enable_backward_forward = models.BooleanField(default=True)
    section_instructions = models.BooleanField(default=False)
    topic_attempt_limits = models.BooleanField(default=False)
    section_wise_break = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Exam Batch Settings'
        verbose_name_plural = 'Exam Batch Settings'


class InternetBasedSettings(TimestampMixin):
    """
    Settings specific to Internet Based Tests
    """
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )
    exam_batch = models.OneToOneField(
        ExamBatch,
        on_delete=models.CASCADE,
        related_name='internet_settings'
    )
    secure_browser = models.BooleanField(default=False)
    warning_enabled = models.BooleanField(default=False)
    allow_proctoring = models.BooleanField(default=False)
    image_based_proctoring = models.BooleanField(default=False)
    video_based_proctoring = models.BooleanField(default=False)
    multi_factor_authentication = models.BooleanField(default=False)
    authentication_type = models.CharField(
        max_length=50,
        choices=AuthenticationType.choices,
        null=True,
        blank=True,
        help_text="Type of authentication required"
    )
    
    # Additional settings
    group_questions_by_subject = models.BooleanField(default=False)
    allow_back_forward = models.BooleanField(default=False)
    show_default_calculator = models.BooleanField(default=False)
    show_scientific_calculator = models.BooleanField(default=False)
    multilingual_test_design = models.BooleanField(default=False)
    all_questions_attempt_mandatory = models.BooleanField(default=False)
    randomize_answer_options = models.BooleanField(default=False)
    show_marks_points = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Internet Based Settings'
        verbose_name_plural = 'Internet Based Settings'


class PaperBasedSettings(TimestampMixin):
    """
    Settings specific to paper-based exams (OSM and Attachment Type)
    """
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )
    exam_batch = models.OneToOneField(
        ExamBatch,
        on_delete=models.CASCADE,
        related_name='paper_settings'
    )
    partial_result_publish = models.BooleanField(default=False)
    passing_marks = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True
    )
    allow_grace_marks = models.BooleanField(default=False)
    upload_sample_answer_sheet = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Paper Based Settings'
        verbose_name_plural = 'Paper Based Settings'


class EvaluatorSettings(TimestampMixin):
    """
    Settings for exam evaluators
    """
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )
    exam_batch = models.OneToOneField(
        ExamBatch,
        on_delete=models.CASCADE,
        related_name='evaluator_settings'
    )
    photo_capture_interval = models.IntegerField(
        help_text="Evaluator photo capture interval in minutes",
        null=True,
        blank=True
    )
    daily_evaluation_limit = models.IntegerField(
        null=True,
        blank=True
    )
    attentive_score = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True
    )
    evaluation_instructions = models.TextField(
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Evaluator Settings'
        verbose_name_plural = 'Evaluator Settings'


class ModeratorSettings(TimestampMixin):
    """
    Settings for exam moderators
    """
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )
    exam_batch = models.OneToOneField(
        ExamBatch,
        on_delete=models.CASCADE,
        related_name='moderator_settings'
    )
    is_enabled = models.BooleanField(default=False)
    assigned_moderator_count = models.IntegerField(
        null=True,
        blank=True
    )
    scripts_allocation_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
        help_text="Percentage of scripts allocated to moderator"
    )
    assign_fresh_script = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Moderator Settings'
        verbose_name_plural = 'Moderator Settings'


class ScannerSettings(TimestampMixin):
    """
    Settings for exam scanners
    """
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )
    exam_batch = models.OneToOneField(
        ExamBatch,
        on_delete=models.CASCADE,
        related_name='scanner_settings'
    )
    is_enabled = models.BooleanField(default=False)
    minimum_script_scanning_page_limit = models.IntegerField(
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Scanner Settings'
        verbose_name_plural = 'Scanner Settings'


class SelectionCriteria(TimestampMixin):
    """
    Model to store selection criteria settings
    """
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )
    exam_batch = models.OneToOneField(
        ExamBatch,
        on_delete=models.CASCADE,
        related_name='selection_criteria'
    )
    criteria_type = models.CharField(
        max_length=50,
        choices=CriteriaType.choices,
        help_text="Type of criteria",
        null=True,
        blank=True
    )
    operator = models.CharField(
        max_length=10,
        choices=ComparisonOperator.choices,
        help_text="Comparison operator",
        null=True,
        blank=True
    )
    value = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        help_text="Criteria value (e.g., 95%)",
        null=True,
        blank=True
    )
    logical_operator = models.CharField(
        max_length=10,
        choices=LogicalOperator.choices,
        help_text="Logical operator for combining criteria",
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Selection Criteria'
        verbose_name_plural = 'Selection Criteria'
