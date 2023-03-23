from rest_framework import serializers
from .models import Company, Employee

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    # To get the company_id to show up in the JSON, we need to add a field to the serializer
    company_id = serializers.ReadOnlyField()

    class Meta:
        model = Company
        fields = "__all__"

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    # To get the employee_id to show up in the JSON, we need to add a field to the serializer
    employee_id = serializers.ReadOnlyField()
    
    class Meta:
        model = Employee
        fields = "__all__"