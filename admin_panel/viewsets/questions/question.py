from rest_framework import viewsets

from admin_panel.models import Question
from admin_panel.serializers.questions import QuestionSerializer


class QuestionViewset(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
