from rest_framework.routers import DefaultRouter
from authentication.views import InstitutionViewSet


router = DefaultRouter()
router.register('institutions', InstitutionViewSet, basename='institutions')


urlpatterns = []

urlpatterns += router.urls
