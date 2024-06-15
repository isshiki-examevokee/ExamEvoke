from rest_framework import viewsets, filters

from admin_panel.models import User
from admin_panel.serializers.candidate.user import UserSerializer


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'last_name']
