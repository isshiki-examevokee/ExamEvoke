from django_filters.rest_framework import DjangoFilterBackend
from admin_panel.batches.model import Batch


from rest_framework import filters, serializers, viewsets

from admin_panel.courses.serializer import CourseSerializer


class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = "__all__"


class BatchResponseSerializer(serializers.ModelSerializer):
    course = CourseSerializer()

    class Meta:
        model = Batch
        fields = "__all__"


class BatchViewset(viewsets.ModelViewSet):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = '__all__'

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return BatchResponseSerializer
        return BatchSerializer