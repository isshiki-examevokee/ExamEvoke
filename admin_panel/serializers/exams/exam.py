from rest_framework import serializers

from admin_panel.models import Exam
from admin_panel.models.exams.exam import ExamConfiguration
from admin_panel.serializers.university.organization import OrganizationSerializer


class ExamConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamConfiguration
        fields = "__all__"


class ExamSerializer(serializers.ModelSerializer):
    config = ExamConfigurationSerializer()

    class Meta:
        model = Exam
        fields = "__all__"


class ExamReponseSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer()

    class Meta:
        model = Exam
        fields = "__all__"

