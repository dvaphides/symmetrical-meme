from rest_framework.routers import DefaultRouter
from .views import UserViewSet, TeamViewSet, ActivityViewSet, WorkoutViewSet, LeaderboardViewSet
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, include
from rest_framework.response import Response
from rest_framework.decorators import api_view

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'workouts', WorkoutViewSet)
router.register(r'leaderboard', LeaderboardViewSet)

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': '/api/users/',
        'teams': '/api/teams/',
        'activities': '/api/activities/',
        'workouts': '/api/workouts/',
        'leaderboard': '/api/leaderboard/',
    })

urlpatterns = [
    path('', api_root, name='api-root'),
    path('', include(router.urls)),
]
