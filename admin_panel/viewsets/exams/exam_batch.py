from rest_framework import viewsets

from admin_panel.models import ExamBatch
from admin_panel.serializers.exams.exam_batch import (
    ExamBatchSerializer,
    ExamBatchResponseSerializer
) 


class ExamBatchViewset(viewsets.ModelViewSet):
    queryset = ExamBatch.objects.all()
    serializer_class = ExamBatchSerializer

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ExamBatchResponseSerializer
        return ExamBatchSerializer
