from admin_panel.courses.model import Course


from rest_framework import serializers

from admin_panel.organizations.serializer import OrganizationSerializer


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class CourseResponseSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer()

    class Meta:
        model = Course
        fields = "__all__"
