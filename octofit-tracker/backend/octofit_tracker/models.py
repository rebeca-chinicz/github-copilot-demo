"""
Models for the OctoFit Tracker application.

Defines data models for users, teams, activities, leaderboard, and workouts.
"""
from djongo import models


class User(models.Model):
    """User model for OctoFit Tracker"""
    _id = models.ObjectIdField()
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.username


class Team(models.Model):
    """Team model for OctoFit Tracker"""
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'teams'

    def __str__(self):
        return self.name


class Activity(models.Model):
    """Activity model for OctoFit Tracker"""
    _id = models.ObjectIdField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=100)
    duration = models.IntegerField()  # Duration in minutes
    distance = models.FloatField(blank=True, null=True)  # Distance in miles
    calories = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'activities'

    def __str__(self):
        return f"{self.user.username} - {self.activity_type}"


class Leaderboard(models.Model):
    """Leaderboard model for OctoFit Tracker"""
    _id = models.ObjectIdField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='leaderboard')
    score = models.IntegerField(default=0)
    rank = models.IntegerField(blank=True, null=True)
    total_activities = models.IntegerField(default=0)
    total_duration = models.IntegerField(default=0)  # Total minutes
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'leaderboard'

    def __str__(self):
        return f"{self.user.username} - Score: {self.score}"


class Workout(models.Model):
    """Workout model for OctoFit Tracker"""
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    difficulty_level = models.CharField(
        max_length=20,
        choices=[('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')],
        default='medium'
    )
    duration = models.IntegerField()  # Duration in minutes
    target_audience = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'workouts'

    def __str__(self):
        return self.name
