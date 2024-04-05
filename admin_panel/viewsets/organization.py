from rest_framework import viewsets

from admin_panel.models.organization import Organization
from admin_panel.serializers.organization import OrganizationSerializer


class OrganizationViewset(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
