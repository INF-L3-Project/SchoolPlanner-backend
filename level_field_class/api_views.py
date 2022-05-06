from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, ListModelMixin, DestroyModelMixin, UpdateModelMixin
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from level_field_class.models import Field, Grade, Group, Level
from level_field_class.serializers import FieldSerializer, GradeSerializer, GroupSerializer, LevelSerializer
from django_filters.rest_framework import DjangoFilterBackend


class FieldViewSet(CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, ListModelMixin,
                   DestroyModelMixin, viewsets.GenericViewSet):
    serializer_class = FieldSerializer
    queryset = Field.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['$name']



class LevelViewSet(CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, ListModelMixin,
                   DestroyModelMixin, viewsets.GenericViewSet):
    serializer_class = LevelSerializer
    queryset = Level.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['$name']


class GradeViewSet(CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, ListModelMixin,
                   DestroyModelMixin, viewsets.GenericViewSet):
    serializer_class = GradeSerializer
    queryset = Grade.objects.all()


class GroupViewSet(CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, ListModelMixin,
                   DestroyModelMixin, viewsets.GenericViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()