from rest_framework import serializers
from level_field_class.models import Field, Grade, Group, Level


class FieldSerializer(serializers.ModelSerializer):

    class Meta:
        model = Field
        fields = ('id', 'name', 'abr')


class LevelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Level
        fields = ('id', 'name', 'abr')


class GradeSerializer(serializers.ModelSerializer):

    name = serializers.ReadOnlyField()

    class Meta:
        model = Grade
        fields = ('id', 'field', 'level', 'capacity', 'name')

    def create(self, validated_data):
        field_data = str(validated_data['field'])[0:3].upper()
        name_data = field_data + "-" + str(validated_data['level']).upper()
        return Grade.objects.create(name=name_data,
                                    capacity=validated_data['capacity'],
                                    level=validated_data['level'],
                                    field=validated_data['field'])


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'name', 'capacity', 'grade')

    def validate(self, data):
        """Check if the capacity of the group is possible for the selected grade"""
        groups = Group.objects.all().filter(grade=data['grade'])
        if groups:
            all_capacity = 0
            for group in groups:
                all_capacity += group.capacity
            if (all_capacity + data['capacity']) > data['grade'].capacity:
                raise serializers.ValidationError(
                    "This capacity is too large for this group")
        elif data['capacity'] > data['grade'].capacity:
            raise serializers.ValidationError(
                "Capacity of the group cannot be higher than that of the class"
            )
        return data
