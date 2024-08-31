from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from admin_panel.models import Topic
from admin_panel.serializers.university.topic import TopicSerializer, TopicResponseSerializer


class TopicViewset(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return TopicResponseSerializer
        return TopicSerializer
