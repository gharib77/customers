import django_filters
from .models import Personne


class FpersFilter(django_filters.FilterSet):
    nom = django_filters.CharFilter(field_name='nom',lookup_expr='contains',label='Nom :')

    class Meta:
        model = Personne
        fields = '__all__'

class PersonneFilter(django_filters.FilterSet):
    class Meta:
        model = Personne
        fields = ['nom']
