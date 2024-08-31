from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from admin_panel.models import Batch
from admin_panel.serializers.university.batch import BatchResponseSerializer, BatchSerializer


class BatchViewset(viewsets.ModelViewSet):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = '__all__'

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return BatchResponseSerializer
        return BatchSerializer