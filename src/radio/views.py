from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import *
from .serializers import *

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'

class RadioStationWebViewSet(viewsets.ModelViewSet):

    queryset = RadioStationModel.objects.all()
    serializer_class = RadioSerializer
    pagination_class = StandardResultsSetPagination

class RadioStationMobileViewSet(viewsets.ModelViewSet):

    queryset = RadioStationModel.objects.all()
    serializer_class = RadioSerializer
    pagination_class = StandardResultsSetPagination

class FavouritesViewSet(viewsets.ModelViewSet):

    queryset = FavouritesModel.objects.all()
    serializer_class = FavouritesSerializer
    pagination_class = StandardResultsSetPagination