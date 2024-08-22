from rest_framework import serializers

from admin_panel.models import Course
from admin_panel.serializers.university.organization import OrganizationSerializer


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class CourseResponseSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer()

    class Meta:
        model = Course
        fields = "__all__"
