from rest_framework import serializers

from admin_panel.models import Topic
from admin_panel.serializers.university.batch import BatchSerializer


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = "__all__"


class TopicResponseSerializer(serializers.ModelSerializer):
    batch = BatchSerializer()

    class Meta:
        model = Topic
        fields = "__all__"
