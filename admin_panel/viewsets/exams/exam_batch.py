from rest_framework import viewsets

from admin_panel.models import ExamBatch
from admin_panel.serializers.exams.exam_batch import ExamBatchSerializer 


class ExamBatchViewset(viewsets.ModelViewSet):
    queryset = ExamBatch.objects.all()
    serializer_class = ExamBatchSerializer
