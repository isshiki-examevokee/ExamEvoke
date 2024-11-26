from admin_panel.questions.model import Question


from rest_framework import serializers

from admin_panel.subjects.serializer import SubjectSerializer
from admin_panel.topics.serializer import TopicSerializer


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