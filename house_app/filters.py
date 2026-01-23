from django_filters import filterset
from .models import Property

class PropertyFilter(filterset.FilterSet):
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
