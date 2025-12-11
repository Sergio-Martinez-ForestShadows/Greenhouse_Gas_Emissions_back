from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination

from .models import Emission
from .serializers import EmissionSerializer


class EmissionPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = "page_size"
    max_page_size = 1000


class EmissionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Read-only API for greenhouse gas emissions.

    Optional filters (query params):
    - country
    - activity
    - emission_type
    - year
    """

    queryset = Emission.objects.all()
    serializer_class = EmissionSerializer
    pagination_class = EmissionPagination
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["year", "country", "emission_type"]

    def get_queryset(self):
        qs = super().get_queryset()
        country = self.request.query_params.get("country")
        activity = self.request.query_params.get("activity")
        emission_type = self.request.query_params.get("emission_type")
        year = self.request.query_params.get("year")

        if country:
            qs = qs.filter(country__iexact=country)
        if activity:
            qs = qs.filter(activity__iexact=activity)
        if emission_type:
            qs = qs.filter(emission_type__iexact=emission_type)
        if year:
            qs = qs.filter(year=year)

        return qs
