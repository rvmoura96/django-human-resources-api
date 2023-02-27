from django_filters import rest_framework as filters

from core.models import Employee, Department


class EmployeeFilter(filters.FilterSet):
    city = filters.CharFilter(field_name='city', lookup_expr='icontains')
    department = filters.ModelChoiceFilter(
        queryset=Department.objects.all(),
        empty_label="Todos os departamentos",
        label="Departamento" ,
        field_name="department"
    )

    class Meta:
        model = Employee
        fields = ('city', 'department')