from admin_panel.organizations.model import Organization


from django.db import models


import uuid


class Subject(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        help_text="The organization to which a subject belongs to",
    )
    code = models.CharField(max_length=255, default='BT101')
    active = models.BooleanField(default=True)