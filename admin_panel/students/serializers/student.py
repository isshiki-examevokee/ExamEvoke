from rest_framework import serializers

from admin_panel.serializers.university.batch import BatchResponseSerializer
from admin_panel.students.models.student import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class StudentResponseSerializer(serializers.ModelSerializer):

    batch = BatchResponseSerializer()
    class Meta:
        model = Student
        fields = "__all__"
