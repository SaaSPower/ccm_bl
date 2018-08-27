from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from chambermaid import views
from django.contrib.auth import views as authviews

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'patients', views.PatientViewSet)
router.register(r'nestedpatients', views.NestedPatientViewSet)
router.register(r'ratingscales', views.RatingScaleViewSet)
router.register(r'nestedratingscales', views.NestedRatingScaleViewSet)
router.register(r'statements', views.StatementViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'nestedprojects', views.NestedProjectViewSet)
router.register(r'project-ratingscale', views.ProjectRatingScaleViewSet)
router.register(r'types', views.TypeViewSet)
router.register(r'typegroups', views.TypeGroupViewSet)
router.register(r'nestedtypegroups', views.NestedTypeGroupViewSet)
router.register(r'cases', views.CaseViewSet)
router.register(r'nestedcases', views.NestedCaseViewSet)
router.register(r'case-type', views.CaseTypeViewSet)
router.register(r'answersheets', views.AnswerSheetViewSet)
router.register(r'answersheets', views.NestedAnswerSheetViewSet)

urlpatterns = [
    url('', include('django.contrib.auth.urls')),
    url('account/login', authviews.LoginView.as_view()),
    url(r'^', include(router.urls)),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),

]