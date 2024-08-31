from rest_framework import serializers

from admin_panel.models import Topic
from admin_panel.serializers.university.subject import SubjectSerializer


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = "__all__"


class TopicResponseSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer()

    class Meta:
        model = Topic
        fields = "__all__"
