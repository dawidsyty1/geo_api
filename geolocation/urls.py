from rest_framework.routers import SimpleRouter
from geolocation import views

router = SimpleRouter()

router.register('', views.GeolocationDataView, 'geolocation')

urlpatterns = router.urls
