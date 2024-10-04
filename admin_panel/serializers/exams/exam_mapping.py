from rest_framework import serializers

from admin_panel.models.exams.exam_mapping import ExamBatchMapping, ExamBatchStudentMapping, ExamQuestionMapping


class ExamBatchMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamBatchMapping
        fields = "__all__"


class ExamQuestionMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamQuestionMapping
        fields = "__all__"


class ExamBatchStudentMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamBatchStudentMapping
        fields = "__all__"

