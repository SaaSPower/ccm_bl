from django.db import models
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.reverse import reverse


class APIRootView(APIView):
    def get(self, request):
        data = {
            'user-list': reverse('user-list', request=request),
        }
        return Response(data)
