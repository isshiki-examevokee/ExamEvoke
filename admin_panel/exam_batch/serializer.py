

from rest_framework import serializers
from admin_panel.batches.serializer import BatchResponseSerializer
from admin_panel.exam_batch.model import ExamBatch
from admin_panel.exams.serializer import ExamResponseSerializer


class ExamBatchCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamBatch
        fields = ['exam', 'batch']


class ExamBatchResponseSerializer(serializers.ModelSerializer):
    exam = ExamResponseSerializer()
    batch = BatchResponseSerializer()
    student_count = serializers.SerializerMethodField()

    class Meta:
        model = ExamBatch
        fields = [
            'id',
            'exam',
            'batch',
            'start_date',
            'end_date',
            'student_count',
            'created_at',
            'updated_at'
        ]

    def get_student_count(self, obj):
        return obj.exam_students.count()


from rest_framework import serializers
from admin_panel.exam_batch.model import (
    ExamBatch, ExamBatchSettings, InternetBasedSettings, 
    PaperBasedSettings, EvaluatorSettings, ModeratorSettings,
    ScannerSettings, SelectionCriteria
)

class SelectionCriteriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SelectionCriteria
        exclude = ['id', 'exam_batch', 'created_at', 'updated_at']


class ExamBatchSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamBatchSettings
        exclude = ['id', 'exam_batch', 'created_at', 'updated_at']


class InternetBasedSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternetBasedSettings
        exclude = ['id', 'exam_batch', 'created_at', 'updated_at']


class PaperBasedSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaperBasedSettings
        exclude = ['id', 'exam_batch', 'created_at', 'updated_at']


class EvaluatorSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EvaluatorSettings
        exclude = ['id', 'exam_batch', 'created_at', 'updated_at']


class ModeratorSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModeratorSettings
        exclude = ['id', 'exam_batch', 'created_at', 'updated_at']


class ScannerSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScannerSettings
        exclude = ['id', 'exam_batch', 'created_at', 'updated_at']


class ExamBatchSettingsRequestSerializer(serializers.Serializer):
    # Basic exam batch schedule
    start_date = serializers.DateField(required=True)
    end_date = serializers.DateField(required=True)
    start_time = serializers.TimeField(required=True)
    end_time = serializers.TimeField(required=True)
    
    # Evaluation schedule (optional)
    evaluation_start_date = serializers.DateField(required=False)
    evaluation_end_date = serializers.DateField(required=False)
    evaluation_start_time = serializers.TimeField(required=False)
    evaluation_end_time = serializers.TimeField(required=False)
    
    # Common settings for all exam types
    common_settings = ExamBatchSettingsSerializer(required=False)
    
    # Mode specific settings
    internet_settings = InternetBasedSettingsSerializer(required=False)
    paper_settings = PaperBasedSettingsSerializer(required=False)
    
    # Evaluation related settings
    evaluator_settings = EvaluatorSettingsSerializer(required=False)
    moderator_settings = ModeratorSettingsSerializer(required=False)
    scanner_settings = ScannerSettingsSerializer(required=False)
    
    # Selection criteria
    selection_criteria = SelectionCriteriaSerializer(required=False)

    def validate(self, data):
        exam_batch = self.context.get('exam_batch')
        if not exam_batch:
            raise serializers.ValidationError("Exam batch context is required")
            
        # Validate settings based on exam mode
        mode = exam_batch.mode
        if mode in ['INTERNET_BASED', 'INTERNET_BASED_HYBRID']:
            if not data.get('internet_settings'):
                raise serializers.ValidationError("Internet settings are required for internet based exams")
        
        if mode in ['PAPER_BASED_OSM', 'PAPER_BASED_OMR', 'PAPER_BASED_ATTACHMENT']:
            if not data.get('paper_settings'):
                raise serializers.ValidationError("Paper settings are required for paper based exams")
            
            # Validate evaluation schedule for paper based exams
            if not all([
                data.get('evaluation_start_date'),
                data.get('evaluation_end_date'),
                data.get('evaluation_start_time'),
                data.get('evaluation_end_time')
            ]):
                raise serializers.ValidationError(
                    "Evaluation schedule is required for paper based exams"
                )
        
        return data
