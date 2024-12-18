# Generated by Django 5.0.4 on 2024-11-26 01:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("admin_panel", "0026_examconfiguration_exam_config"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="exam",
            name="config",
        ),
        migrations.RemoveField(
            model_name="exam",
            name="organization",
        ),
        migrations.RemoveField(
            model_name="exambatchmapping",
            name="exam",
        ),
        migrations.RemoveField(
            model_name="examquestionmapping",
            name="exam",
        ),
        migrations.RemoveField(
            model_name="exambatch",
            name="exam",
        ),
        migrations.RemoveField(
            model_name="exambatchstudentmapping",
            name="exambatch",
        ),
        migrations.RemoveField(
            model_name="exambatchmapping",
            name="exambatch",
        ),
        migrations.RemoveField(
            model_name="exambatchmapping",
            name="organization",
        ),
        migrations.RemoveField(
            model_name="exambatchstudentmapping",
            name="organization",
        ),
        migrations.RemoveField(
            model_name="exambatchstudentmapping",
            name="student",
        ),
        migrations.RemoveField(
            model_name="examquestionmapping",
            name="exambatch",
        ),
        migrations.RemoveField(
            model_name="examquestionmapping",
            name="organization",
        ),
        migrations.DeleteModel(
            name="ExamConfiguration",
        ),
        migrations.DeleteModel(
            name="Exam",
        ),
        migrations.DeleteModel(
            name="ExamBatch",
        ),
        migrations.DeleteModel(
            name="ExamBatchMapping",
        ),
        migrations.DeleteModel(
            name="ExamBatchStudentMapping",
        ),
        migrations.DeleteModel(
            name="ExamQuestionMapping",
        ),
    ]
