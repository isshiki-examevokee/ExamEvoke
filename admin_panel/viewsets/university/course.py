from rest_framework import viewsets

from admin_panel.models import Course
from admin_panel.serializers.university.course import CourseSerializer


class CourseViewset(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
