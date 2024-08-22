from rest_framework import serializers

from admin_panel.models import Question
from admin_panel.serializers.university.subject import SubjectSerializer
from admin_panel.serializers.university.topic import TopicSerializer


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


class QuestionResponseSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer()
    topic = TopicSerializer()

    class Meta:
        model = Question
        fields = "__all__"
