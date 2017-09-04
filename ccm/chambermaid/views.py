from rest_framework import viewsets
from chambermaid.serializers import *
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


class TypeViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class CaseViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Case.objects.all()
    serializer_class = CaseSerializer


class AnswerSheetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = AnswerSheet.objects.all()
    serializer_class = AnswerSheetSerializer

