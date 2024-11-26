# Generated by Django 5.0.4 on 2024-11-26 03:31

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("admin_panel", "0027_remove_exam_config_remove_exam_organization_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Exam",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "name",
                    models.CharField(help_text="Name of the exam", max_length=255),
                ),
                (
                    "objective",
                    models.CharField(
                        choices=[
                            ("Semester Exam", "Semester Exam"),
                            ("Mock Exam", "Mock Exam"),
                            ("Entrance Exam", "Entrance Exam"),
                            ("Test Series", "Test Series"),
                        ],
                        help_text="Purpose of the exam",
                        max_length=50,
                    ),
                ),
                ("duration", models.DurationField(help_text="Duration of the exam")),
                (
                    "difficulty",
                    models.CharField(
                        choices=[
                            ("Easy", "Easy"),
                            ("Medium", "Medium"),
                            ("Hard", "Hard"),
                        ],
                        help_text="Difficulty level of the exam",
                        max_length=20,
                    ),
                ),
                (
                    "department",
                    models.CharField(
                        help_text="Department conducting the exam", max_length=255
                    ),
                ),
                (
                    "semester",
                    models.CharField(
                        help_text="Semester for which exam is being conducted",
                        max_length=50,
                    ),
                ),
                (
                    "subject",
                    models.CharField(help_text="Subject of the exam", max_length=255),
                ),
                (
                    "exam_code",
                    models.CharField(
                        help_text="Unique code for the exam", max_length=50, unique=True
                    ),
                ),
                (
                    "total_questions",
                    models.PositiveIntegerField(
                        help_text="Total number of questions in the exam",
                        validators=[django.core.validators.MinValueValidator(1)],
                    ),
                ),
                (
                    "total_marks",
                    models.PositiveIntegerField(
                        help_text="Total marks for the exam",
                        validators=[django.core.validators.MinValueValidator(1)],
                    ),
                ),
                (
                    "organization",
                    models.ForeignKey(
                        help_text="Organization conducting the exam",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="admin_panel.organization",
                    ),
                ),
            ],
            options={
                "verbose_name": "Exam",
                "verbose_name_plural": "Exams",
                "ordering": ["-created_at"],
            },
        ),
    ]
