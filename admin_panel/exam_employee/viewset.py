from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status, serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db import transaction
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from django_filters.rest_framework import DjangoFilterBackend

from admin_panel.exam_employee.model import ExamEmployee, ExamEmployeeRole
from admin_panel.exam_employee.serializer import ExamEmployeeAssignmentSerializer, ExamEmployeeResponseSerializer
from admin_panel.exams.model import Exam
from admin_panel.users.models.employee import Employee



class ExamEmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoints for managing employee assignments to exams
    """
    queryset = ExamEmployee.objects.all()
    serializer_class = ExamEmployeeResponseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['exam', 'role']

    @swagger_auto_schema(
        tags=['Exam Employees'],
        operation_summary="Assign employees to exam",
        operation_description="Assign multiple employees to an exam with a specific role",
        request_body=ExamEmployeeAssignmentSerializer,
        responses={
            201: ExamEmployeeResponseSerializer(many=True),
            400: "Bad Request - Invalid data or validation error",
            404: "Not Found - Exam does not exist"
        }
    )
    @action(detail=False, methods=['post'], url_path='assign')
    @transaction.atomic
    def assign_employees(self, request):
        serializer = ExamEmployeeAssignmentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        exam = get_object_or_404(Exam, id=serializer.validated_data['exam_id'])
        employee_ids = serializer.validated_data['employee_ids']
        role = serializer.validated_data['role']
        
        # Delete existing assignments for this role
        ExamEmployee.objects.filter(exam=exam, role=role).delete()
        
        # Create new assignments
        new_assignments = []
        for employee_id in employee_ids:
            employee = Employee.objects.get(id=employee_id)
            assignment = ExamEmployee.objects.create(
                exam=exam,
                employee=employee,
                role=role,
                organization=exam.organization
            )
            new_assignments.append(assignment)
        
        response_serializer = ExamEmployeeResponseSerializer(
            new_assignments, 
            many=True
        )
        return Response(
            response_serializer.data,
            status=status.HTTP_201_CREATED
        )

    @swagger_auto_schema(
        tags=['Exam Employees'],
        operation_summary="Get exam employees by role",
        operation_description="Get list of employees assigned to an exam by role",
        manual_parameters=[
            openapi.Parameter(
                'exam_id',
                openapi.IN_QUERY,
                description="UUID of the exam",
                type=openapi.TYPE_STRING,
                required=True
            ),
            openapi.Parameter(
                'role',
                openapi.IN_QUERY,
                description="Role of the employees (EVALUATOR, MODERATOR, SCANNER)",
                type=openapi.TYPE_STRING,
                required=True,
                enum=[choice[0] for choice in ExamEmployeeRole.choices]
            )
        ],
        responses={
            200: ExamEmployeeResponseSerializer(many=True),
            400: "Bad Request - Missing or invalid parameters",
            404: "Not Found - Exam does not exist"
        }
    )
    @action(detail=False, methods=['get'], url_path='by-role')
    def get_employees_by_role(self, request):
        exam_id = request.query_params.get('exam_id')
        role = request.query_params.get('role')

        if not exam_id or not role:
            return Response(
                {"error": "Both exam_id and role are required query parameters"},
                status=status.HTTP_400_BAD_REQUEST
            )

        exam = get_object_or_404(Exam, id=exam_id)
        
        try:
            assignments = ExamEmployee.objects.filter(
                exam=exam,
                role=role.upper()
            )
        except ValueError:
            return Response(
                {"error": f"Invalid role. Must be one of {[choice[0] for choice in ExamEmployeeRole.choices]}"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = self.get_serializer(assignments, many=True)
        return Response(serializer.data)
