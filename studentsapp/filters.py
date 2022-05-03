from django import forms
from studentsapp.models import FCN
import django_filters
 
 
class FCNFilter(django_filters.FilterSet):
    cbank = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    cinvestor = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    cCND = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.NumberInput(attrs={'class': 'form-control'}))
    class Meta:
        model = FCN
        fields = '__all__'
