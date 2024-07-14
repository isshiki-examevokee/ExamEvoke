from rest_framework import viewsets

from admin_panel.models import Exam
from admin_panel.serializers.exams.exam import ExamSerializer


class ExamViewset(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
