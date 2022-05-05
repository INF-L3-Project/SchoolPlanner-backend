from rest_framework.routers import DefaultRouter
from level_field_class.api_views import FieldViewSet, GradeViewSet, GroupViewSet, LevelViewSet

router = DefaultRouter()
router.register('fields', FieldViewSet, basename='fields')
router.register('levels', LevelViewSet, basename='levels')
router.register('grades', GradeViewSet, basename='grades')
router.register('groups', GroupViewSet, basename='groups')

urlpatterns = []

urlpatterns += router.urls