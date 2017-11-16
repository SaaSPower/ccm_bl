from rest_framework import serializers
from django.contrib.auth.models import User
from chambermaid.models import *


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', )


class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = '__all__'


class StatementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Statement
        fields = '__all__'


class RatingScaleSerializer(serializers.ModelSerializer):

    class Meta:
        model = RatingScale
        fields = '__all__'


class NestedRatingScaleSerializer(serializers.ModelSerializer):
    statements = StatementSerializer(many=True, read_only=True)

    class Meta:
        model = RatingScale
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'


class ProjectRatingScaleSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectRatingScale
        fields = '__all__'


class TypeGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = TypeGroup
        fields = '__all__'


class TypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Type
        fields = '__all__'


class NestedTypeGroupSerializer(serializers.ModelSerializer):
    types = TypeSerializer(many=True, read_only=True)

    class Meta:
        model = TypeGroup
        fields = '__all__'


class CaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Case
        fields = '__all__'


class AnswerSheetSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnswerSheet
        fields = '__all__'


class NestedAnswerSheetSerializer(serializers.ModelSerializer):
    rating_scale = NestedRatingScaleSerializer()

    class Meta:
        model = AnswerSheet
        fields = '__all__'


class NestedCaseSerializer(serializers.ModelSerializer):
    answersheets = NestedAnswerSheetSerializer(many=True, read_only=True)

    class Meta:
        model = Case
        fields = '__all__'


class NestedProjectSerializer(serializers.ModelSerializer):
    cases = CaseSerializer(many=True, read_only=True)
    rating_scales = NestedRatingScaleSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = '__all__'


class NestedPatientSerializer(serializers.ModelSerializer):
    cases = NestedCaseSerializer(many=True, read_only=True)

    class Meta:
        model = Patient
        fields = '__all__'


class CaseTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = CaseType
        fields = '__all__'




