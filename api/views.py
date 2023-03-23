from django.shortcuts import render
from rest_framework.response import Response

from rest_framework import viewsets
from api.serializers import CompanySerializer, EmployeeSerializer
from api.models import Company, Employee
from rest_framework.decorators import action

# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


    #Defining a custom url for the company viewset
    #companies/{company_id}/employee
    @action(detail = True, methods = ['get'])
    def employees(self, request, pk = None):

        print("This is for retrieving all employees of a company")
        try:
            company = Company.objects.get(pk = pk)
            emps = Employee.objects.filter(company = company)
            emps_serializer = EmployeeSerializer(emps, many = True, context = {'request' : request})
            return Response(emps_serializer.data)
        except Exception as e:
            print(e)
            return Response({'message' : 'Company does not exist'})

        

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

