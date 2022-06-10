from pyexpat import model
import django_filters
from .models import CS_IT_Course
from django_filters import CharFilter

class CS_IT_Filter(django_filters.FilterSet):
    Name = CharFilter(field_name='courseName', lookup_expr='icontains')
    class Meta:
        model = CS_IT_Course
        fields = '__all__'