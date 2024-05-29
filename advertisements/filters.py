from django_filters import rest_framework as filters
import django_filters
from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    created_at = filters.DateFromToRangeFilter()
    status = django_filters.ChoiceFilter(field_name="status", choices=Advertisement.STATUS_CHOICES)

    class Meta:
        model = Advertisement
        fields = ['created_at', 'status']
