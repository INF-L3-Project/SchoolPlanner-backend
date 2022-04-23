from rest_framework.routers import DefaultRouter
from authentication.api_views import (InstitutionViewSet, LoginAPIView, LogoutAPIView)
from django.urls import path


router = DefaultRouter()
router.register('accounts', InstitutionViewSet, basename='accounts')

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name="login"),
    path('logout/', LogoutAPIView.as_view(), name="logout"),

]

urlpatterns += router.urls
