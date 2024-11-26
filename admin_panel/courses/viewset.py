
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from admin_panel.courses.model import Course
from admin_panel.courses.serializer import CourseResponseSerializer, CourseSerializer


class CourseViewset(viewsets.ModelViewSet):
    """
    API endpoints for managing courses in the system.
    Supports filtering on all available fields.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return CourseResponseSerializer
        return CourseSerializer

    @swagger_auto_schema(
        tags=['Courses'],
        operation_summary="List courses",
        operation_description="Returns a list of all courses. Supports filtering on all available fields.",
        responses={200: CourseResponseSerializer(many=True)},
        manual_parameters=[
            openapi.Parameter(
                'filter',
                openapi.IN_QUERY,
                description="Filter courses by any available field",
                type=openapi.TYPE_OBJECT,
                required=False
            )
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Courses'],
        operation_summary="Create course",
        operation_description="Create a new course record",
        request_body=CourseSerializer,
        responses={
            201: CourseSerializer,
            400: "Bad Request - Invalid data"
        }
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Courses'],
        operation_summary="Get course details",
        operation_description="Retrieve details of a specific course by ID",
        responses={
            200: CourseResponseSerializer,
            404: "Not Found - Course does not exist"
        }
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Courses'],
        operation_summary="Update course",
        operation_description="Update all fields of a specific course",
        request_body=CourseSerializer,
        responses={
            200: CourseSerializer,
            400: "Bad Request - Invalid data",
            404: "Not Found - Course does not exist"
        }
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Courses'],
        operation_summary="Partial update course",
        operation_description="Update specific fields of a course",
        request_body=CourseSerializer,
        responses={
            200: CourseSerializer,
            400: "Bad Request - Invalid data",
            404: "Not Found - Course does not exist"
        }
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Courses'],
        operation_summary="Delete course",
        operation_description="Remove a course record",
        responses={
            204: "No content - Successfully deleted",
            404: "Not Found - Course does not exist"
        }
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
