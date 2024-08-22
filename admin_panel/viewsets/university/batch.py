from rest_framework import viewsets

from admin_panel.models import Batch
from admin_panel.serializers.university.batch import BatchResponseSerializer, BatchSerializer


class BatchViewset(viewsets.ModelViewSet):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return BatchResponseSerializer
        return BatchSerializer