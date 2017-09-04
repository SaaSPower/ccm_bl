from rest_framework import serializers
from django.contrib.auth.models import User
from chambermaid.models import Patient, RatingScale, Statement, Project, Type, Case, AnswerSheet


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'email', )


class PatientSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Patient
        fields = '__all__'


class RatingScaleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = RatingScale
        fields = '__all__'


class StatementSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Statement
        fields = '__all__'


class ProjectSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'


class TypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Type
        fields = '__all__'


class CaseSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Case
        fields = '__all__'


class AnswerSheetSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = AnswerSheet
        fields = '__all__'

