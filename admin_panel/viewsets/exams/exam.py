from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from admin_panel.models import Exam
from admin_panel.serializers.exams.exam import (
    ExamSerializer,
    ExamReponseSerializer,
)


class ExamViewset(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ExamReponseSerializer
        return ExamSerializer
