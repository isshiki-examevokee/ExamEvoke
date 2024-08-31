from rest_framework import serializers

from admin_panel.models import Subject
from admin_panel.serializers.university.organization import OrganizationSerializer


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"


class SubjectResponseSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer()

    class Meta:
        model = Subject
        fields = "__all__"
