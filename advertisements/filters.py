from django_filters import rest_framework as filters

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    date = filters.DateFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ['date']
