import uuid

from django.db import models

from admin_panel.models.exams.exam import Exam


class ExamBatch(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )
    exam = models.ForeignKey(
        Exam,
        related_name="exambatches",
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        blank=False,
        null=False,
        max_length=255,
    )
    start = models.DateTimeField(blank=True, null=True)
    end = models.DateTimeField(blank=True, null=True)
    details = models.TextField()
    mode = models.CharField(
        blank=False,
        null=False,
        max_length=255,   
    )
    start_date = models.DateField(
        blank=True,
        null=True,
    )
    start_time = models.TimeField(
        blank=True,
        null=True,
    )
    end_date = models.DateField(
        blank=True,
        null=True,
    )
    end_time = models.TimeField(
        blank=True,
        null=True,
    )
    batch_conf = models.JSONField()
