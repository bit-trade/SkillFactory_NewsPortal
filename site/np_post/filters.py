from django_filters import FilterSet, DateFilter
from django.forms import DateInput
from .models import Post


class PublicFilter(FilterSet):
    date_creation = DateFilter(
        field_name='date_creation',
        lookup_expr='date__lt',
        widget=DateInput(attrs={'type': 'date'}),
        label='Дата'
    )

    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'author__full_name': ['contains'],
        }
