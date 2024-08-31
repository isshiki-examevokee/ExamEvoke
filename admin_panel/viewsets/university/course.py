from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from admin_panel.models import Course
from admin_panel.serializers.university.course import (
    CourseResponseSerializer,
    CourseSerializer,
)


class CourseViewset(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return CourseResponseSerializer
        return CourseSerializer
