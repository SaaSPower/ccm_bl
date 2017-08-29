from rest_framework import viewsets
from django.contrib.auth.models import User
from chambermaid.serializers import UserSerializer, PatientSerializer
from chambermaid.models import Patient


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PatientViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

