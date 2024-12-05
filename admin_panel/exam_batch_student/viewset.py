from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, viewsets
from rest_framework.response import Response
from admin_panel.exam_batch_student.model import ExamStudent
from admin_panel.exam_batch_student.serializer import ExamStudentResponseSerializer, ExamStudentSerializer


class ExamStudentViewSet(viewsets.ModelViewSet):
    """
    API endpoints for managing individual student participation in exams.
    """
    queryset = ExamStudent.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['exam_batch', 'student', 'exam_batch__exam']

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return ExamStudentSerializer
        return ExamStudentResponseSerializer

    @swagger_auto_schema(
        tags=['Exam Students'],
        operation_summary="List exam students",
        operation_description="Get a list of all exam students with optional filtering by exam batch, student, and exam",
        responses={
            200: ExamStudentResponseSerializer(many=True),
            400: "Bad Request - Invalid filter parameters"
        }
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Exam Students'],
        operation_summary="Get exam student details",
        operation_description="Retrieve detailed information about a specific exam student",
        responses={
            200: ExamStudentResponseSerializer,
            404: "Not Found - Exam student does not exist"
        }
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Exam Students'],
        operation_summary="Add student to exam batch",
        operation_description="Add a single student to an exam batch",
        request_body=ExamStudentSerializer,
        responses={
            201: ExamStudentResponseSerializer,
            400: "Bad Request - Student already in 2 batches for this exam"
        }
    )
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # Check if student already belongs to 2 batches for this exam
        student = serializer.validated_data['student']
        exam_batch = serializer.validated_data['exam_batch']
        existing_count = ExamStudent.objects.filter(
            student=student,
            exam_batch__exam=exam_batch.exam
        ).count()
        
        if existing_count >= 2:
            return Response(
                {"error": "Student cannot be added to more than two batches for the same exam"},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        exam_student = serializer.save()
        response_serializer = ExamStudentResponseSerializer(exam_student)
        return Response(
            response_serializer.data,
            status=status.HTTP_201_CREATED
        )
