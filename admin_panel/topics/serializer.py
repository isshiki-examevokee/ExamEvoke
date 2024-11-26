from admin_panel.subjects.serializer import SubjectSerializer
from admin_panel.topics.model import Topic


from rest_framework import serializers


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = "__all__"


class TopicResponseSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer()

    class Meta:
        model = Topic
        fields = "__all__"