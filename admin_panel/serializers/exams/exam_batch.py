from rest_framework import serializers

from admin_panel.models import ExamBatch
from admin_panel.serializers.exams.exam import ExamSerializer


class ExamBatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamBatch
        fields = "__all__"


class ExamBatchResponseSerializer(serializers.ModelSerializer):
    exam = ExamSerializer()

    class Meta:
        model = ExamBatch
        fields = "__all__"
