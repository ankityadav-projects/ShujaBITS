from rest_framework import serializers

from employee.models import Emp

class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emp
        fields = ['name', 'email', 'doj', 'location']
        