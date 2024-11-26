from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from admin_panel.topics.model import Topic
from admin_panel.topics.serializer import TopicResponseSerializer, TopicSerializer


class TopicViewset(viewsets.ModelViewSet):
    """
    API endpoints for managing topics in the system.
    Supports filtering on all available fields.
    """
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return TopicResponseSerializer
        return TopicSerializer

    @swagger_auto_schema(
        tags=['Topics'],
        operation_summary="List topics",
        operation_description="Returns a list of all topics. Supports filtering on all available fields.",
        responses={
            200: TopicResponseSerializer(many=True)
        },
        manual_parameters=[
            openapi.Parameter(
                'filter',
                openapi.IN_QUERY,
                description="Filter topics by any available field (e.g., subject_id, name)",
                type=openapi.TYPE_OBJECT,
                required=False
            )
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Topics'],
        operation_summary="Create topic",
        operation_description="Create a new topic record. Topics are linked to specific subjects.",
        request_body=TopicSerializer,
        responses={
            201: TopicSerializer,
            400: "Bad Request - Invalid data provided",
            403: "Forbidden - Insufficient permissions"
        }
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Topics'],
        operation_summary="Get topic details",
        operation_description="Retrieve details of a specific topic by ID",
        responses={
            200: TopicResponseSerializer,
            404: "Not Found - Topic does not exist"
        }
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Topics'],
        operation_summary="Update topic",
        operation_description="Update all fields of a specific topic",
        request_body=TopicSerializer,
        responses={
            200: TopicSerializer,
            400: "Bad Request - Invalid data provided",
            403: "Forbidden - Insufficient permissions",
            404: "Not Found - Topic does not exist"
        }
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Topics'],
        operation_summary="Partial update topic",
        operation_description="Update specific fields of a topic",
        request_body=TopicSerializer,
        responses={
            200: TopicSerializer,
            400: "Bad Request - Invalid data provided",
            403: "Forbidden - Insufficient permissions",
            404: "Not Found - Topic does not exist"
        }
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Topics'],
        operation_summary="Delete topic",
        operation_description="Remove a topic record",
        responses={
            204: "No content - Successfully deleted",
            403: "Forbidden - Insufficient permissions",
            404: "Not Found - Topic does not exist"
        }
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
