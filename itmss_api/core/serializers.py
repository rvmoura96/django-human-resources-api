from rest_framework import serializers

from .models import Department, Employee, HeadQuarter


class HeadQuarterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HeadQuarter
        fields = "__all__"


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"