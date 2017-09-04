from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from chambermaid import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'patients', views.PatientViewSet)
router.register(r'ratingscales', views.RatingScaleViewSet)
router.register(r'statements', views.StatementViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'types', views.TypeViewSet)
router.register(r'cases', views.CaseViewSet)
router.register(r'answersheets', views.AnswerSheetViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]