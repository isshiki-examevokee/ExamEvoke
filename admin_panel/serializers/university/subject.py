from rest_framework import serializers

from admin_panel.models import Subject
from admin_panel.serializers.university.batch import BatchSerializer


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"


class SubjectResponseSerializer(serializers.ModelSerializer):
    batch = BatchSerializer()

    class Meta:
        model = Subject
        fields = "__all__"
