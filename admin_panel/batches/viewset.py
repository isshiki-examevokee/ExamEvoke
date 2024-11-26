from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from admin_panel.batches.model import Batch
from admin_panel.batches.serializer import (
    BatchResponseSerializer,
    BatchSerializer,
)


class BatchViewset(viewsets.ModelViewSet):
    """
    API endpoints for managing batches in the system.
    Supports filtering on all fields and searching.
    """
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = '__all__'

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return BatchResponseSerializer
        return BatchSerializer

    @swagger_auto_schema(
        tags=['Batches'],
        operation_summary="List batches",
        operation_description="Returns a list of all batches. Supports filtering on all fields and searching.",
        responses={200: BatchResponseSerializer(many=True)},
        manual_parameters=[
            openapi.Parameter(
                'search',
                openapi.IN_QUERY,
                description="Search in available fields",
                type=openapi.TYPE_STRING,
                required=False
            ),
            openapi.Parameter(
                'filter',
                openapi.IN_QUERY,
                description="Filter batches by any available field",
                type=openapi.TYPE_OBJECT,
                required=False
            )
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Batches'],
        operation_summary="Create batch",
        operation_description="Create a new batch record",
        request_body=BatchSerializer,
        responses={
            201: BatchSerializer,
            400: "Bad Request - Invalid data provided",
            403: "Forbidden - Insufficient permissions"
        }
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Batches'],
        operation_summary="Get batch details",
        operation_description="Retrieve details of a specific batch by ID",
        responses={
            200: BatchResponseSerializer,
            404: "Not Found - Batch does not exist"
        }
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Batches'],
        operation_summary="Update batch",
        operation_description="Update all fields of a specific batch",
        request_body=BatchSerializer,
        responses={
            200: BatchSerializer,
            400: "Bad Request - Invalid data provided",
            403: "Forbidden - Insufficient permissions",
            404: "Not Found - Batch does not exist"
        }
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Batches'],
        operation_summary="Partial update batch",
        operation_description="Update specific fields of a batch",
        request_body=BatchSerializer,
        responses={
            200: BatchSerializer,
            400: "Bad Request - Invalid data provided",
            403: "Forbidden - Insufficient permissions",
            404: "Not Found - Batch does not exist"
        }
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Batches'],
        operation_summary="Delete batch",
        operation_description="Remove a batch record",
        responses={
            204: "No content - Successfully deleted",
            403: "Forbidden - Insufficient permissions",
            404: "Not Found - Batch does not exist"
        }
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)