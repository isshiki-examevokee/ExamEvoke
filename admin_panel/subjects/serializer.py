from admin_panel.subjects.model import Subject


from rest_framework import serializers

from admin_panel.organizations.serializer import OrganizationSerializer


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"


class SubjectResponseSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer()

    class Meta:
        model = Subject
        fields = "__all__"