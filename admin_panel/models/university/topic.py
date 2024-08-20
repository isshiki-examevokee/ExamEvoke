import uuid

from django.db import models

from admin_panel.models.university.batch import Batch


class Topic(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    batch = models.ForeignKey(
        Batch,
        on_delete=models.CASCADE,
        help_text="The subject to which a topic belongs to",
    )
    active = models.BooleanField(default=True)
