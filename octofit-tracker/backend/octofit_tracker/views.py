"""
Views for the OctoFit Tracker API.

Handles all HTTP requests and returns appropriate responses.
"""
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .serializers import (
    UserSerializer,
    TeamSerializer,
    ActivitySerializer,
    LeaderboardSerializer,
    WorkoutSerializer,
)
from .models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId


@api_view(['GET'])
def api_root(request, format=None):
    """
    API root endpoint displaying all available endpoints.
    """
    # Use the request's scheme and host for dynamic URL generation
    scheme = request.scheme
    host = request.get_host()
    base_url = f'{scheme}://{host}/'
    
    return Response({
        'users': base_url + 'api/users/?format=api',
        'teams': base_url + 'api/teams/?format=api',
        'activities': base_url + 'api/activities/?format=api',
        'leaderboard': base_url + 'api/leaderboard/?format=api',
        'workouts': base_url + 'api/workouts/?format=api'
    })


class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for User model.
    Provides CRUD operations for users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = '_id'

    def get_object(self):
        """Override to support MongoDB ObjectId lookup"""
        pk = self.kwargs.get(self.lookup_field)
        try:
            # Try to convert to ObjectId
            obj_id = ObjectId(pk)
            try:
                return User.objects.get(_id=obj_id)
            except User.DoesNotExist:
                raise NotFound('User not found.')
        except Exception:
            raise NotFound('Invalid user ID format.')


class TeamViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Team model.
    Provides CRUD operations for teams.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    lookup_field = '_id'

    def get_object(self):
        """Override to support MongoDB ObjectId lookup"""
        pk = self.kwargs.get(self.lookup_field)
        try:
            obj_id = ObjectId(pk)
            try:
                return Team.objects.get(_id=obj_id)
            except Team.DoesNotExist:
                raise NotFound('Team not found.')
        except Exception:
            raise NotFound('Invalid team ID format.')


class ActivityViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Activity model.
    Provides CRUD operations for activities.
    """
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    lookup_field = '_id'

    def get_object(self):
        """Override to support MongoDB ObjectId lookup"""
        pk = self.kwargs.get(self.lookup_field)
        try:
            obj_id = ObjectId(pk)
            try:
                return Activity.objects.get(_id=obj_id)
            except Activity.DoesNotExist:
                raise NotFound('Activity not found.')
        except Exception:
            raise NotFound('Invalid activity ID format.')


class LeaderboardViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Leaderboard model.
    Provides read and update operations for leaderboard entries.
    """
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer
    lookup_field = '_id'

    def get_object(self):
        """Override to support MongoDB ObjectId lookup"""
        pk = self.kwargs.get(self.lookup_field)
        try:
            obj_id = ObjectId(pk)
            try:
                return Leaderboard.objects.get(_id=obj_id)
            except Leaderboard.DoesNotExist:
                raise NotFound('Leaderboard entry not found.')
        except Exception:
            raise NotFound('Invalid leaderboard ID format.')


class WorkoutViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Workout model.
    Provides CRUD operations for workouts.
    """
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    lookup_field = '_id'

    def get_object(self):
        """Override to support MongoDB ObjectId lookup"""
        pk = self.kwargs.get(self.lookup_field)
        try:
            obj_id = ObjectId(pk)
            try:
                return Workout.objects.get(_id=obj_id)
            except Workout.DoesNotExist:
                raise NotFound('Workout not found.')
        except Exception:
            raise NotFound('Invalid workout ID format.')
