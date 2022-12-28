from rest_framework.routers import DefaultRouter

from radio.views import *

webApprouter = DefaultRouter(trailing_slash=False)
webApprouter.register(r'station', RadioStationWebViewSet, basename="station")

mobileApprouter = DefaultRouter(trailing_slash=False)
mobileApprouter.register(
    r'stations', RadioStationMobileViewSet, basename="stations")
mobileApprouter.register(
    r'favStations', FavouritesViewSet, basename="favStations")
