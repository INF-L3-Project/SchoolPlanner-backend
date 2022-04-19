from rest_framework import serializers
from authentication.models import Institution


class InstitutionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Institution
        fields = '__all__'


