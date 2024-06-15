from rest_framework import viewsets, filters

from admin_panel.models import Student
from admin_panel.serializers.user.student import StudentSerializer


class StudentViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'last_name']
