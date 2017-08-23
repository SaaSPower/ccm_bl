from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from chambermaid.serializers import UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
