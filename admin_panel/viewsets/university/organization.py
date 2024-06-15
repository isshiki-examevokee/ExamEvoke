from rest_framework import viewsets

from admin_panel.models import Organization
from admin_panel.serializers.university.organization import OrganizationSerializer


class OrganizationViewset(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
