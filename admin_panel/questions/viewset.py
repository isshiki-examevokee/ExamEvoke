from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from admin_panel.questions.model import Question
from admin_panel.questions.serializer import QuestionResponseSerializer, QuestionSerializer


class QuestionViewset(viewsets.ModelViewSet):
    """
    API endpoints for managing questions in the system.
    Provides CRUD operations for exam questions with different serializers for list/retrieve vs create/update operations.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = []

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return QuestionResponseSerializer
        return QuestionSerializer

    @swagger_auto_schema(
        tags=['Questions'],
        operation_summary="List questions",
        operation_description="Returns a list of all questions in the system.",
        responses={
            200: QuestionResponseSerializer(many=True)
        }
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Questions'],
        operation_summary="Create question",
        operation_description="Create a new question record. This includes the question text, options, correct answer, and other relevant details.",
        request_body=QuestionSerializer,
        responses={
            201: QuestionSerializer,
            400: "Bad Request - Invalid data provided",
            403: "Forbidden - Insufficient permissions"
        }
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Questions'],
        operation_summary="Get question details",
        operation_description="Retrieve details of a specific question by ID, including its options and correct answer.",
        responses={
            200: QuestionResponseSerializer,
            404: "Not Found - Question does not exist"
        }
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Questions'],
        operation_summary="Update question",
        operation_description="Update all fields of a specific question, including question text, options, and correct answer.",
        request_body=QuestionSerializer,
        responses={
            200: QuestionSerializer,
            400: "Bad Request - Invalid data provided",
            403: "Forbidden - Insufficient permissions",
            404: "Not Found - Question does not exist"
        }
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Questions'],
        operation_summary="Partial update question",
        operation_description="Update specific fields of a question. Useful for modifying individual aspects like question text or options.",
        request_body=QuestionSerializer,
        responses={
            200: QuestionSerializer,
            400: "Bad Request - Invalid data provided",
            403: "Forbidden - Insufficient permissions",
            404: "Not Found - Question does not exist"
        }
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Questions'],
        operation_summary="Delete question",
        operation_description="Remove a question record. This will also remove the question from any associated exams.",
        responses={
            204: "No content - Successfully deleted",
            403: "Forbidden - Insufficient permissions",
            404: "Not Found - Question does not exist"
        }
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
