import uuid

from django.db import models

from admin_panel.models.university.batch import Batch


class Subject(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )
    serial_no = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    batch = models.ForeignKey(
        Batch,
        on_delete=models.CASCADE,
        help_text="The batch to which a subject belongs to",
    )
    code = models.CharField(max_length=255, default='BT101')
    active = models.BooleanField(default=True)
