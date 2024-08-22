from rest_framework import viewsets

from admin_panel.models import Question
from admin_panel.serializers.questions import (
    QuestionSerializer,
    QuestionResponseSerializer,
)


class QuestionViewset(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return QuestionResponseSerializer
        return QuestionSerializer
