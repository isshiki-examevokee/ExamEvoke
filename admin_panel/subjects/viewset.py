from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from admin_panel.subjects.model import Subject
from admin_panel.subjects.serializer import SubjectResponseSerializer, SubjectSerializer


class SubjectViewset(viewsets.ModelViewSet):
    """
    API endpoints for managing subjects in the system.
    Supports filtering on all available fields.
    """
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return SubjectResponseSerializer
        return SubjectSerializer

    @swagger_auto_schema(
        tags=['Subjects'],
        operation_summary="List subjects",
        operation_description="Returns a list of all subjects. Supports filtering on all available fields.",
        responses={
            200: SubjectResponseSerializer(many=True)
        },
        manual_parameters=[
            openapi.Parameter(
                'filter',
                openapi.IN_QUERY,
                description="Filter subjects by any available field",
                type=openapi.TYPE_OBJECT,
                required=False
            )
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Subjects'],
        operation_summary="Create subject",
        operation_description="Create a new subject record",
        request_body=SubjectSerializer,
        responses={
            201: SubjectSerializer,
            400: "Bad Request - Invalid data provided",
            403: "Forbidden - Insufficient permissions"
        }
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Subjects'],
        operation_summary="Get subject details",
        operation_description="Retrieve details of a specific subject by ID",
        responses={
            200: SubjectResponseSerializer,
            404: "Not Found - Subject does not exist"
        }
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Subjects'],
        operation_summary="Update subject",
        operation_description="Update all fields of a specific subject",
        request_body=SubjectSerializer,
        responses={
            200: SubjectSerializer,
            400: "Bad Request - Invalid data provided",
            403: "Forbidden - Insufficient permissions",
            404: "Not Found - Subject does not exist"
        }
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Subjects'],
        operation_summary="Partial update subject",
        operation_description="Update specific fields of a subject",
        request_body=SubjectSerializer,
        responses={
            200: SubjectSerializer,
            400: "Bad Request - Invalid data provided",
            403: "Forbidden - Insufficient permissions",
            404: "Not Found - Subject does not exist"
        }
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Subjects'],
        operation_summary="Delete subject",
        operation_description="Remove a subject record",
        responses={
            204: "No content - Successfully deleted",
            403: "Forbidden - Insufficient permissions",
            404: "Not Found - Subject does not exist"
        }
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
