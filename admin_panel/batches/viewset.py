from admin_panel.batches.model import Batch
from admin_panel.batches.serializer import (
    BatchResponseSerializer,
    BatchSerializer,
)


from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets


class BatchViewset(viewsets.ModelViewSet):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = '__all__'

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return BatchResponseSerializer
        return BatchSerializer