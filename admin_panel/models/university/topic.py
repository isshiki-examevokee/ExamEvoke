import uuid

from django.db import models

from admin_panel.models.university.subject import Subject


class Topic(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )
    serial_no = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    batch = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        help_text="The subject to which a topic belongs to",
    )
    active = models.BooleanField(default=True)
