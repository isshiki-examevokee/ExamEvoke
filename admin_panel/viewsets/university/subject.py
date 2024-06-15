from rest_framework import viewsets

from admin_panel.models import Subject
from admin_panel.serializers.university.subject import SubjectSerializer


class SubjectViewset(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
