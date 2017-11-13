from rest_framework import serializers
from django.contrib.auth.models import User
from chambermaid.models import *


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
    rating_scale_id = serializers.PrimaryKeyRelatedField(queryset=RatingScale.objects.all())

    class Meta:
        model = Statement
        fields = '__all__'


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    rating_scales = RatingScaleSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = '__all__'


class ProjectRatingScaleSerializer(serializers.HyperlinkedModelSerializer):
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())
    rating_scale = serializers.PrimaryKeyRelatedField(queryset=RatingScale.objects.all())

    class Meta:
        model = ProjectRatingScale
        fields = '__all__'


class TypeGroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = TypeGroup
        fields = ('url', 'id', 'group_code', 'description')


class TypeSerializer(serializers.HyperlinkedModelSerializer):
    type_group = TypeGroupSerializer(read_only=True)
    type_group_id = serializers.PrimaryKeyRelatedField(read_only=False, queryset=TypeGroup.objects.all(),
                                                       allow_null=False)

    class Meta:
        model = Type
        fields = '__all__'
        depth = 1


class CaseSerializer(serializers.HyperlinkedModelSerializer):
    patient = PatientSerializer(read_only=True)
    project = ProjectSerializer(read_only=True)
    types = TypeSerializer(many=True)
    patient_id = serializers.PrimaryKeyRelatedField(read_only=False, queryset=Patient.objects.all(),
                                                    allow_null=False)
    project_id = serializers.PrimaryKeyRelatedField(read_only=False, queryset=Project.objects.all(),
                                                    allow_null=False)

    class Meta:
        model = Case
        fields = '__all__'
        depth = 1


class CaseTypeSerializer(serializers.HyperlinkedModelSerializer):
    case = serializers.PrimaryKeyRelatedField(queryset=Case.objects.all())
    type = serializers.PrimaryKeyRelatedField(queryset=Type.objects.all())

    class Meta:
        model = CaseType
        fields = '__all__'


class AnswerSheetSerializer(serializers.HyperlinkedModelSerializer):
    case_id = serializers.IntegerField()
    rating_scale_id = serializers.IntegerField()

    class Meta:
        model = AnswerSheet
        fields = '__all__'