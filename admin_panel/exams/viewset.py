# viewsets.py
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from admin_panel.exams.model import Exam
from admin_panel.exams.serializer import ExamCreateSerializer, ExamResponseSerializer, ExamSerializer


class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['organization', 'difficulty', 'objective']

    def get_serializer_class(self):
        if self.action in ['create']:
            return ExamCreateSerializer
        if self.action in ['update', 'partial_update']:
            return ExamSerializer
        return ExamResponseSerializer

    @swagger_auto_schema(
        tags=['Exam'],
        operation_description="API endpoint for retrieving exam list",
        responses={200: ExamResponseSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Exam'],
        operation_description="API endpoint for creating an exam",
        responses={201: ExamResponseSerializer}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Exam'],
        operation_description="API endpoint for retrieving exam details",
        responses={200: ExamResponseSerializer}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Exam'],
        operation_description="API endpoint for updating exam details",
        responses={200: ExamResponseSerializer}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Exam'],
        request_body=ExamSerializer(partial=True),
        operation_description="API endpoint for partially updating exam details",
        operation_id="admin_panel_exam_partial_update",
        responses={200: ExamResponseSerializer}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Exam'],
        operation_description="API endpoint for deleting an exam",
        responses={204: ""}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
