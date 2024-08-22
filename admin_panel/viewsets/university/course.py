from rest_framework import viewsets

from admin_panel.models import Course
from admin_panel.serializers.university.course import (
    CourseSerializer,
    CourseResponseSerializer,
)


class CourseViewset(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return CourseResponseSerializer
        return CourseSerializer
