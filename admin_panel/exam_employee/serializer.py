from rest_framework import serializers
from admin_panel.exam_employee.model import ExamEmployee, ExamEmployeeRole
from admin_panel.users.serializers.employee import EmployeeResponseSerializer


from rest_framework import serializers



class ExamEmployeeAssignmentSerializer(serializers.Serializer):
    """
    Serializer for assigning multiple employees to an exam with a specific role
    """
    exam_id = serializers.UUIDField(
        help_text="UUID of the exam to assign employees to"
    )
    employee_ids = serializers.ListField(
        child=serializers.UUIDField(),
        help_text="List of employee IDs to assign"
    )
    role = serializers.ChoiceField(
        choices=ExamEmployeeRole.choices,
        help_text="Role to assign to the employees"
    )


class ExamEmployeeResponseSerializer(serializers.ModelSerializer):
    employee = EmployeeResponseSerializer()
    
    class Meta:
        model = ExamEmployee
        fields = ['id', 'employee', 'role', 'created_at', 'updated_at']