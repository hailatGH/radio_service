from rest_framework.routers import DefaultRouter

from player.views import *
# from player.mobileAppviews import *

webApprouter = DefaultRouter(trailing_slash=False)
webApprouter.register(r'station', RadioStationViewSet, basename="station")

mobileApprouter = DefaultRouter(trailing_slash=False)
mobileApprouter.register(r'favStations', FavouritesViewSet, basename="favStations")