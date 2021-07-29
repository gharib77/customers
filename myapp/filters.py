import django_filters
from .models import Personne


class FpersFilter(django_filters.FilterSet):
    nom = django_filters.CharFilter(field_name='nom',lookup_expr='contains',label='Nom :')

    class Meta:
        model = Personne
        fields = '__all__'
