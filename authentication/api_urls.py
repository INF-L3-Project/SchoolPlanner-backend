from rest_framework.routers import DefaultRouter
from authentication.api_views import (InstitutionViewSet, LoginAPIView,
                                      LogoutAPIView, PasswordTokenCheckAPI,
                                      RequestPasswordResetEmail,
                                      SetNewPasswordAPIView)
from django.urls import path

router = DefaultRouter()
router.register('accounts', InstitutionViewSet, basename='accounts')

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name="login"),
    path('logout/', LogoutAPIView.as_view(), name="logout"),
    path('request-reset-email/',
         RequestPasswordResetEmail.as_view(),
         name="request-reset-email"),
    path('password-reset/<uidb64>/<token>/',
         PasswordTokenCheckAPI.as_view(),
         name='password-reset-confirm'),
    path('password-reset-complete',
         SetNewPasswordAPIView.as_view(),
         name='password-reset-complete')
]

urlpatterns += router.urls
