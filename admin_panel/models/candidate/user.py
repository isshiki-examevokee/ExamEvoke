import uuid

from django.db import models


class UserRole(models.TextChoices):
    EVALUATOR = "EVALUATOR"
    SCANNER = "SCANNER"


class User(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    role = models.CharField(
        choices=UserRole.choices,
        max_length=255,
        default=UserRole.EVALUATOR,
    )
