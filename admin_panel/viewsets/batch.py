from rest_framework import viewsets

from admin_panel.models import Batch
from admin_panel.serializers.batch import BatchSerializer


class BatchViewset(viewsets.ModelViewSet):
    queryset = Batch
    serializer_class = BatchSerializer
