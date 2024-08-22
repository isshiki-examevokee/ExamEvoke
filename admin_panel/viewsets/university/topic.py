from rest_framework import viewsets

from admin_panel.models import Topic
from admin_panel.serializers.university.topic import TopicSerializer, TopicResponseSerializer


class TopicViewset(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return TopicResponseSerializer
        return TopicSerializer
