from django.urls import path
from rest_framework.routers import DefaultRouter
# from rest_framework_swagger.views import get_swagger_view

from .views import SubjectViewSet, ScoreViewSet, StudentViewSet

app_name = 'students'

router = DefaultRouter()
router.register('students', StudentViewSet, basename='students')
router.register('scores', ScoreViewSet, basename='scores')
router.register('subjects', SubjectViewSet, basename='subjects')

# swagger_view = get_swagger_view(title="Student Scores API")

urlpatterns = [
    # path('docs/', swagger_view),
] + router.urls