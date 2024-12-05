from rest_framework import serializers
from admin_panel.exams.model import Exam
from admin_panel.organizations.serializer import OrganizationSerializer
from django.db import models


class ExamCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating an exam"""
    class Meta:
        model = Exam
        fields = [
            'name',
            'objective',
            'duration',
            'difficulty',
            'department',
            'semester',
            'subject',
            'exam_code',
            'total_questions',
            'total_marks',
            'organization'
        ]

    def validate(self, data):
        if data.get('total_marks', 0) < data.get('total_questions', 0):
            raise serializers.ValidationError(
                "Total marks cannot be less than total questions"
            )
        return data


class ExamSerializer(serializers.ModelSerializer):
    """Serializer for updating exam data"""
    class Meta:
        model = Exam
        fields = "__all__"

    def validate(self, data):
        if all(k in data for k in ['total_marks', 'total_questions']):
            if data['total_marks'] < data['total_questions']:
                raise serializers.ValidationError(
                    "Total marks cannot be less than total questions"
                )
        return data


class ExamResponseSerializer(serializers.ModelSerializer):
    """Serializer for reading exam data"""
    organization = OrganizationSerializer(read_only=True)
    batch_count = serializers.SerializerMethodField()
    student_count = serializers.SerializerMethodField()

    class Meta:
        model = Exam
        fields = [
            'id',
            'name',
            'objective',
            'duration',
            'difficulty',
            'department',
            'semester',
            'subject',
            'exam_code',
            'total_questions',
            'total_marks',
            'organization',
            'created_at',
            'updated_at',
            'batch_count',
            'student_count'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def get_batch_count(self, obj):
        return obj.exam_batches.count()

    def get_student_count(self, obj):
        return getattr(
            obj,
            'student_count',
            obj.exam_batches.aggregate(
                total_students=models.Count('exam_students')
            )['total_students'] or 0
        )
