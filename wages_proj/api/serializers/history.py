from rest_framework import serializers

from database.models import Salary


class HistorySalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Salary
        fields = '__all__'
