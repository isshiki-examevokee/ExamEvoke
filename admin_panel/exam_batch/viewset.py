from django.db import transaction
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, viewsets
from rest_framework.response import Response
from admin_panel.exam_batch.model import ExamBatch
from admin_panel.exam_batch.serializer import ExamBatchCreateSerializer, ExamBatchResponseSerializer
from admin_panel.exam_batch_student.model import ExamStudent


class ExamBatchViewSet(viewsets.ModelViewSet):
    """
    API endpoints for managing exam-batch relationships.
    """
    queryset = ExamBatch.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['exam', 'batch']

    def get_serializer_class(self):
        if self.action == 'create':
            return ExamBatchCreateSerializer
        return ExamBatchResponseSerializer

    @swagger_auto_schema(
        tags=['Exam Batches'],
        operation_summary="Add batch to exam",
        operation_description="Add a batch to an exam and optionally clone its students",
        request_body=ExamBatchCreateSerializer,
        responses={
            201: ExamBatchResponseSerializer,
            400: "Bad Request - Invalid data or validation error"
        }
    )
    @transaction.atomic
    def create(self, request, *args, **kwargs):
        clone_students = request.data.pop('clone_students', True)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        exam_batch = serializer.save()

        if clone_students:
            batch_students = exam_batch.batch.student.all()
            exam_students = []
            
            for student in batch_students:
                # Check if student already has 2 batches for this exam
                existing_count = ExamStudent.objects.filter(
                    student=student,
                    exam_batch__exam=exam_batch.exam
                ).count()
                
                if existing_count < 2:
                    exam_students.append(
                        ExamStudent(
                            exam_batch=exam_batch,
                            student=student
                        )
                    )
            
            if exam_students:
                ExamStudent.objects.bulk_create(exam_students)

        response_serializer = ExamBatchResponseSerializer(exam_batch)
        return Response(
            response_serializer.data,
            status=status.HTTP_201_CREATED,
        )