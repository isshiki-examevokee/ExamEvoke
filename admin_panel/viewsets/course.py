from rest_framework import viewsets

from admin_panel.models.courses import Course
from admin_panel.serializers.courses import CourseSerializer


class CourseViewset(viewsets.ModelViewSet):
    queryset = Course
    serializer_class = CourseSerializer
