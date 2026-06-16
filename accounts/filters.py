import django_filters
from .models import Orders

class OrderFilter(django_filters.FilterSet):
    class Meta:
        model=Order
        field='__all__'
