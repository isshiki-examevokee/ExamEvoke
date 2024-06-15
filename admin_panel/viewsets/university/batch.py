from rest_framework import viewsets

from admin_panel.models import Batch
from admin_panel.serializers.university.batch import BatchSerializer


class BatchViewset(viewsets.ModelViewSet):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer
