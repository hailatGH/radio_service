from rest_framework.routers import DefaultRouter

from player.views import *

webApprouter = DefaultRouter(trailing_slash=False)
webApprouter.register(r'station', RadioStationViewSet, basename="station")

mobileApprouter = DefaultRouter(trailing_slash=False)
mobileApprouter.register(r'stations', RadioStationViewSet, basename="stations")
mobileApprouter.register(r'favStations', FavouritesViewSet, basename="favStations")