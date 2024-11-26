

from rest_framework import serializers
from admin_panel.exam_batch.serializer import ExamBatchResponseSerializer
from admin_panel.exam_batch_student.model import ExamStudent
from admin_panel.students.serializer import StudentResponseSerializer


class ExamStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamStudent
        fields = ['exam_batch', 'student']


class ExamStudentResponseSerializer(serializers.ModelSerializer):
    exam_batch = ExamBatchResponseSerializer()
    student = StudentResponseSerializer()

    class Meta:
        model = ExamStudent
        fields = ['id', 'exam_batch', 'student', 'created_at', 'updated_at']