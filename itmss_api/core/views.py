from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions


from .filters import EmployeeFilter
from .models import Department, Employee, HeadQuarter
from .serializers import DepartmentSerializer, EmployeeSerializer, HeadQuarterSerializer


class HeadQuarterViewSet(viewsets.ModelViewSet):
    queryset = HeadQuarter.objects.all()
    serializer_class = HeadQuarterSerializer
    permission_classes = [permissions.IsAuthenticated]


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.IsAuthenticated]


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filterset_class = EmployeeFilter
    permission_classes = [permissions.IsAuthenticated]