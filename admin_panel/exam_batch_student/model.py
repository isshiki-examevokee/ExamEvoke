
import uuid
from django.db import models

from admin_panel.exam_batch.model import ExamBatch
from admin_panel.organizations.model import Organization
from admin_panel.students.models.student import Student
from utils.timestamp_mixin import TimestampMixin


class ExamStudent(TimestampMixin):
    """
    Model to track individual students in an exam through their batches
    """
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )
    exam_batch = models.ForeignKey(
        ExamBatch,
        on_delete=models.CASCADE,
        related_name='exam_students'
    )
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='exam_students'
    )
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name='exam_students'
    )

    class Meta:
        unique_together = ['exam_batch', 'student']
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.exam_batch.exam.name} - {self.student.first_name}"
