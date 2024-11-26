from rest_framework import serializers

from admin_panel.models import Batch
from admin_panel.courses.serializer import CourseSerializer


class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = "__all__"


class BatchResponseSerializer(serializers.ModelSerializer):
    course = CourseSerializer()

    class Meta:
        model = Batch
        fields = "__all__"
