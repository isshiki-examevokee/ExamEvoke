import uuid

from django.db import models

from admin_panel.models.user.base import BaseUser


class EmployeeRole(models.TextChoices):
    EVALUATOR = "EVALUATOR"
    SCANNER = "SCANNER"


class Employee(BaseUser):
    role = models.CharField(
        choices=EmployeeRole.choices,
        max_length=255,
        default=EmployeeRole.EVALUATOR,
    )
    signature_picture_url = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
