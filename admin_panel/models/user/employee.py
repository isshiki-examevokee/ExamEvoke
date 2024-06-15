import uuid

from django.db import models


class EmployeeRole(models.TextChoices):
    EVALUATOR = "EVALUATOR"
    SCANNER = "SCANNER"


class Employee(models.Model):
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
        choices=EmployeeRole.choices,
        max_length=255,
        default=EmployeeRole.EVALUATOR,
    )
