

from rest_framework import serializers
from admin_panel.batches.serializer import BatchResponseSerializer
from admin_panel.exam_batch.model import ExamBatch
from admin_panel.exams.serializer import ExamResponseSerializer


class ExamBatchCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamBatch
        fields = ['exam', 'batch']


class ExamBatchResponseSerializer(serializers.ModelSerializer):
    exam = ExamResponseSerializer()
    batch = BatchResponseSerializer()
    student_count = serializers.SerializerMethodField()

    class Meta:
        model = ExamBatch
        fields = [
            'id',
            'exam',
            'batch',
            'start_date',
            'end_date',
            'student_count',
            'created_at',
            'updated_at'
        ]

    def get_student_count(self, obj):
        return obj.exam_students.count()
