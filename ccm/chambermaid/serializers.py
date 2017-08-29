from rest_framework import serializers
from django.contrib.auth.models import User
from chambermaid.models import Patient


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'email', )


class PatientSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Patient
        fields = '__all__'


