from rest_framework import serializers

from admin_panel.models import ExamBatch


class ExamBatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamBatch
        fields = "__all__"
