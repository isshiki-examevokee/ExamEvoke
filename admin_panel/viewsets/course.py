from rest_framework import viewsets

from admin_panel.models.course import Course
from admin_panel.serializers.course import CourseSerializer


class CourseViewset(viewsets.ModelViewSet):
    queryset = Course
    serializer_class = CourseSerializer
