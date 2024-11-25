from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response

from admin_panel.students.models.employee import Employee, EmployeeRole
from admin_panel.students.serializers.employee import EmployeeResponseSerializer, EmployeeSerializer




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

    @action(detail=False, methods=['get'])
    def get_employee_roles(self, request, pk=None):
        roles = [role.value for role in EmployeeRole]
        return Response(roles)
