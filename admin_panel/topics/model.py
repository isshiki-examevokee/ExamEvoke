from admin_panel.subjects.model import Subject


from django.db import models


import uuid


class Topic(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        help_text="The subject to which a topic belongs to",
    )
    active = models.BooleanField(default=True)