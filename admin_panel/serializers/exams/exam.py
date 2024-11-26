from rest_framework import serializers

from admin_panel.models import Exam
from admin_panel.organizations.serializer import OrganizationSerializer


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = "__all__"


class ExamReponseSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer()

    class Meta:
        model = Exam
        fields = "__all__"
