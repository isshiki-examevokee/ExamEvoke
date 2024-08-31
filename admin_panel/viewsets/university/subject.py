from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from admin_panel.models import Subject
from admin_panel.serializers.university.subject import SubjectSerializer, SubjectResponseSerializer


class SubjectViewset(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return SubjectResponseSerializer
        return SubjectSerializer
