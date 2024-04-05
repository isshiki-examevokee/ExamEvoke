from rest_framework import viewsets

from admin_panel.models import Topic
from admin_panel.serializers.subject import TopicSerializer


class TopicViewset(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
