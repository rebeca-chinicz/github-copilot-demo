"""
Django admin configuration for OctoFit Tracker.

Registers models with the Django admin interface for easy management.
"""
from django.contrib import admin
from .models import User, Team, Activity, Leaderboard, Workout


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Admin interface for User model"""
    list_display = ['username', 'email', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['username', 'email']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('User Information', {
            'fields': ('username', 'email', 'password')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    """Admin interface for Team model"""
    list_display = ['name', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['name']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Team Information', {
            'fields': ('name', 'description')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    """Admin interface for Activity model"""
    list_display = ['user', 'activity_type', 'duration', 'created_at']
    list_filter = ['activity_type', 'created_at']
    search_fields = ['user__username', 'activity_type']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Activity Information', {
            'fields': ('user', 'activity_type', 'duration', 'distance', 'calories')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    """Admin interface for Leaderboard model"""
    list_display = ['user', 'rank', 'score', 'total_activities', 'total_duration']
    list_filter = ['rank', 'updated_at']
    search_fields = ['user__username']
    readonly_fields = ['updated_at']
    fieldsets = (
        ('Leaderboard Information', {
            'fields': ('user', 'score', 'rank', 'total_activities', 'total_duration')
        }),
        ('Timestamps', {
            'fields': ('updated_at',),
            'classes': ('collapse',)
        }),
    )


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    """Admin interface for Workout model"""
    list_display = ['name', 'difficulty_level', 'duration', 'created_at']
    list_filter = ['difficulty_level', 'created_at']
    search_fields = ['name', 'target_audience']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Workout Information', {
            'fields': ('name', 'description', 'difficulty_level', 'duration', 'target_audience')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
