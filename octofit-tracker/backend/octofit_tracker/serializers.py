"""
Serializers for the OctoFit Tracker application.

Converts model instances to JSON and vice versa.
"""
from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId


class ObjectIdField(serializers.Field):
    """Custom serializer field for MongoDB ObjectId"""
    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        try:
            return ObjectId(data)
        except Exception:
            self.fail('invalid_object_id', value=data)


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model"""
    _id = ObjectIdField()

    class Meta:
        model = User
        fields = ['_id', 'username', 'email', 'created_at', 'updated_at']
        extra_kwargs = {
            'password': {'write_only': True},
        }


class TeamSerializer(serializers.ModelSerializer):
    """Serializer for Team model"""
    _id = ObjectIdField()

    class Meta:
        model = Team
        fields = ['_id', 'name', 'description', 'created_at', 'updated_at']


class ActivitySerializer(serializers.ModelSerializer):
    """Serializer for Activity model"""
    _id = ObjectIdField()
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        write_only=True,
        source='user'
    )

    class Meta:
        model = Activity
        fields = ['_id', 'user', 'user_id', 'activity_type', 'duration', 'distance', 'calories', 'created_at', 'updated_at']


class LeaderboardSerializer(serializers.ModelSerializer):
    """Serializer for Leaderboard model"""
    _id = ObjectIdField()
    user = UserSerializer(read_only=True)

    class Meta:
        model = Leaderboard
        fields = ['_id', 'user', 'score', 'rank', 'total_activities', 'total_duration', 'updated_at']


class WorkoutSerializer(serializers.ModelSerializer):
    """Serializer for Workout model"""
    _id = ObjectIdField()

    class Meta:
        model = Workout
        fields = ['_id', 'name', 'description', 'difficulty_level', 'duration', 'target_audience', 'created_at', 'updated_at']
