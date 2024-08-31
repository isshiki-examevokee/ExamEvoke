from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend


from admin_panel.models import Employee
from admin_panel.serializers.user.employee import (
    EmployeeSerializer,
    EmployeeResponseSerializer,
)


class EmployeeViewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['first_name', 'last_name']
    filterset_fields = '__all__'

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return EmployeeResponseSerializer
        return EmployeeSerializer
