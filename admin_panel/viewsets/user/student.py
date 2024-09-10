from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from admin_panel.models import Student
from admin_panel.serializers.user.student import StudentResponseSerializer, StudentSerializer


class StudentViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['first_name', 'last_name']
    filterset_fields = '__all__'

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return StudentResponseSerializer
        return StudentSerializer
