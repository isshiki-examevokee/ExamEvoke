# Generated by Django 5.0.4 on 2024-08-14 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("admin_panel", "0013_alter_exam_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="exam",
            name="type",
            field=models.CharField(
                choices=[("SEMESTER", "Semester")], default="SEMESTER", max_length=255
            ),
        ),
    ]
