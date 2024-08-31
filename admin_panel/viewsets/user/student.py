from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from admin_panel.models import Student
from admin_panel.serializers.user.student import StudentSerializer


class StudentViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['first_name', 'last_name']
    filterset_fields = '__all__'
