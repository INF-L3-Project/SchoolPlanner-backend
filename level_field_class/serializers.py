from rest_framework import serializers
from level_field_class.models import Field, Grade, Group, Level


class FieldSerializer(serializers.ModelSerializer):

    class Meta:
        model = Field
        fields = ('id', 'name')


class LevelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Level
        fields = ('id', 'name')


class GradeSerializer(serializers.ModelSerializer):

    level = LevelSerializer()
    field = FieldSerializer()
    
    class Meta:
        model = Grade
        fields = ('id', 'name', 'capacity', 'level', 'field')  


class GroupSerializer(serializers.ModelSerializer):

    grade = GradeSerializer()
    
    class Meta:
        model = Group
        fields = ('id', 'name', 'capacity', 'grade')
