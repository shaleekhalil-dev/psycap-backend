from rest_framework import serializers
from .models import EmployeePsyCap

class EmployeePsyCapSerializer(serializers.ModelSerializer):
    # إضافة الحقول المحسوبة للـ API
    average_score = serializers.ReadOnlyField()
    status = serializers.ReadOnlyField()

    class Meta:
        model = EmployeePsyCap
        fields = ['id', 'name', 'hope', 'efficacy', 'resilience', 'optimism', 'average_score', 'status', 'created_at']
