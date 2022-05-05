from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, ListModelMixin, DestroyModelMixin
from rest_framework import viewsets
from level_field_class.models import Field, Grade, Group, Level
from level_field_class.serializers import FieldSerializer, GradeSerializer, GroupSerializer, LevelSerializer


class FieldViewSet(CreateModelMixin, RetrieveModelMixin, ListModelMixin,
                   DestroyModelMixin, viewsets.GenericViewSet):
    serializer_class = FieldSerializer
    queryset = Field.objects.all()


class LevelViewSet(CreateModelMixin, RetrieveModelMixin, ListModelMixin,
                   DestroyModelMixin, viewsets.GenericViewSet):
    serializer_class = LevelSerializer
    queryset = Level.objects.all()


class GradeViewSet(CreateModelMixin, RetrieveModelMixin, ListModelMixin,
                   DestroyModelMixin, viewsets.GenericViewSet):
    serializer_class = GradeSerializer
    queryset = Grade.objects.all()


class GroupViewSet(CreateModelMixin, RetrieveModelMixin, ListModelMixin,
                   DestroyModelMixin, viewsets.GenericViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()