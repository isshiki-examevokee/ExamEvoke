import uuid

from django.db import models

from admin_panel.models.university.course import Course


class Batch(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        help_text="The course to which a batch belongs to",
    )
    active = models.BooleanField(default=True)
