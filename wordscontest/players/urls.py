from rest_framework import routers

from .views import PlayersViewSet

router = routers.SimpleRouter()
router.register(r'players', PlayersViewSet, 'players')

urlpatterns = router.urls
