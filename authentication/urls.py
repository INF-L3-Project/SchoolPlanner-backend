from django.urls import path
from authentication.views import InstitutionRegisterView
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('register/', InstitutionRegisterView.as_view(), name="register"),
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),

]
