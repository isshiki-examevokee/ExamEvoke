from django.db import models
import uuid


class ExamBatch(models.Model):
    """
    Model to manage the relationship between Exams and Batches
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
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    organization = models.ForeignKey(
        'Organization',
        on_delete=models.CASCADE,
        related_name='exam_batches'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['exam', 'batch']
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.exam.name} - {self.batch.name}"
