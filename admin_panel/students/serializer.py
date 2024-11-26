from admin_panel.batches.serializer import BatchResponseSerializer
from admin_panel.students.models.student import Student


from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class StudentResponseSerializer(serializers.ModelSerializer):

    batch = BatchResponseSerializer()

    class Meta:
        model = Student
        fields = "__all__"