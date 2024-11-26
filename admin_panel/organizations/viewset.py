from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from admin_panel.organizations.model import Organization
from admin_panel.organizations.serializer import OrganizationSerializer


class OrganizationViewset(viewsets.ModelViewSet):
    """
    API endpoints for managing organizations in the system.
    Provides basic CRUD operations for organizations.
    """
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

    @swagger_auto_schema(
        tags=['Organizations'],
        operation_summary="List organizations",
        operation_description="Returns a list of all organizations.",
        responses={
            200: OrganizationSerializer(many=True)
        }
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Organizations'],
        operation_summary="Create organization",
        operation_description="Create a new organization record",
        request_body=OrganizationSerializer,
        responses={
            201: OrganizationSerializer,
            400: "Bad Request - Invalid data provided",
            403: "Forbidden - Insufficient permissions"
        }
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Organizations'],
        operation_summary="Get organization details",
        operation_description="Retrieve details of a specific organization by ID",
        responses={
            200: OrganizationSerializer,
            404: "Not Found - Organization does not exist"
        }
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Organizations'],
        operation_summary="Update organization",
        operation_description="Update all fields of a specific organization",
        request_body=OrganizationSerializer,
        responses={
            200: OrganizationSerializer,
            400: "Bad Request - Invalid data provided",
            403: "Forbidden - Insufficient permissions",
            404: "Not Found - Organization does not exist"
        }
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Organizations'],
        operation_summary="Partial update organization",
        operation_description="Update specific fields of an organization",
        request_body=OrganizationSerializer,
        responses={
            200: OrganizationSerializer,
            400: "Bad Request - Invalid data provided",
            403: "Forbidden - Insufficient permissions",
            404: "Not Found - Organization does not exist"
        }
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Organizations'],
        operation_summary="Delete organization",
        operation_description="Remove an organization record",
        responses={
            204: "No content - Successfully deleted",
            403: "Forbidden - Insufficient permissions",
            404: "Not Found - Organization does not exist"
        }
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)