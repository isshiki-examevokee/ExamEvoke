

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
