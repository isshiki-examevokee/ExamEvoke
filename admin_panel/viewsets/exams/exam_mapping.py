from rest_framework import viewsets
from admin_panel.models.exams.exam_mapping import ExamBatchMapping, ExamBatchStudentMapping, ExamQuestionMapping
from admin_panel.serializers.exams.exam_mapping import (
    ExamBatchMappingSerializer,
    ExamQuestionMappingSerializer,
    ExamBatchStudentMappingSerializer
)
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend


class ExamBatchMappingViewSet(viewsets.ModelViewSet):
    serializer_class = ExamBatchMappingSerializer
    queryset = ExamBatchMapping.objects.all()
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = '__all__'


class ExamQuestionMappingViewSet(viewsets.ModelViewSet):
    serializer_class = ExamQuestionMappingSerializer
    queryset = ExamQuestionMapping.objects.all()
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = '__all__'


class ExamBatchStudentMappingViewSet(viewsets.ModelViewSet):
    serializer_class = ExamBatchStudentMappingSerializer
    queryset = ExamBatchStudentMapping.objects.all()
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = '__all__'
