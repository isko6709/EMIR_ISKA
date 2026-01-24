from django_filters import rest_framework as filters
from .models import Property


class PropertyFilter(filters.FilterSet):
    class Meta:
        model = Property
        fields = {
            'price': ['gt', 'lt'],
            'area': ['gt', 'lt'],
            'rooms': ['gt', 'lt'],
            'property_type': ['exact'],
            'condition': ['exact'],
            'region': ['exact'],
            'city': ['exact'],
            'district': ['exact'],
        }