from rest_framework import viewsets
from chambermaid.serializers import *
from chambermaid.models import Patient
from rest_framework.response import Response


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


class RatingScaleViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = RatingScale.objects.all()
    serializer_class = RatingScaleSerializer


class StatementViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Statement.objects.all()
    serializer_class = StatementSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectRatingScaleViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = ProjectRatingScale.objects.all()
    serializer_class = ProjectRatingScaleSerializer


class TypeViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class TypeGroupViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = TypeGroup.objects.all()
    serializer_class = TypeGroupSerializer


class CaseViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Case.objects.all()
    serializer_class = CaseSerializer


class CaseTypeViewSet(viewsets.ModelViewSet):
    queryset = CaseType.objects.all()
    serializer_class = CaseTypeSerializer


class AnswerSheetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = AnswerSheet.objects.all()
    serializer_class = AnswerSheetSerializer

