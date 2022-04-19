from rest_framework import viewsets
from authentication.Serializers import InstitutionSerializer
from authentication.models import Institution


class InstitutionViewSet(viewsets.ModelViewSet):
    serializer_class = InstitutionSerializer
    queryset = Institution.objects.all()



