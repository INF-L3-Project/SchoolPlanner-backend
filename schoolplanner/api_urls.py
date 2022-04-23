from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="School Planner API",
      default_version='version 1',
      description="Documentation de l'API de School Planner , un service de gestion des emplois de temps dans une ecole",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="parnelltchamba24@gmail"),
      license=openapi.License(name="BSD License"),
   ),
)

urlpatterns = [
    path('', include(('authentication.api_urls', 'authentication'))),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
