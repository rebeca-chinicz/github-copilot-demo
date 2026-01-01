"""
Tests for the OctoFit Tracker application.

Tests API endpoints and model functionality.
"""
from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import User, Team, Activity, Leaderboard, Workout


class UserAPITestCase(APITestCase):
    """Test cases for User API endpoints"""

    def setUp(self):
        """Set up test data"""
        self.user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpass123',
        }

    def test_create_user(self):
        """Test creating a new user"""
        response = self.client.post('/api/users/', self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['username'], self.user_data['username'])

    def test_list_users(self):
        """Test listing all users"""
        response = self.client.get('/api/users/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TeamAPITestCase(APITestCase):
    """Test cases for Team API endpoints"""

    def setUp(self):
        """Set up test data"""
        self.team_data = {
            'name': 'Fitness Team',
            'description': 'A team for fitness enthusiasts',
        }

    def test_create_team(self):
        """Test creating a new team"""
        response = self.client.post('/api/teams/', self.team_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], self.team_data['name'])

    def test_list_teams(self):
        """Test listing all teams"""
        response = self.client.get('/api/teams/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ActivityAPITestCase(APITestCase):
    """Test cases for Activity API endpoints"""

    def setUp(self):
        """Set up test data"""
        self.user = User.objects.create(
            username='testuser',
            email='testuser@example.com',
            password='testpass123',
        )
        self.activity_data = {
            'user_id': str(self.user.id),
            'activity_type': 'running',
            'duration': 30,
            'distance': 5.0,
            'calories': 300,
        }

    def test_create_activity(self):
        """Test creating a new activity"""
        response = self.client.post('/api/activities/', self.activity_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['activity_type'], self.activity_data['activity_type'])

    def test_list_activities(self):
        """Test listing all activities"""
        response = self.client.get('/api/activities/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class WorkoutAPITestCase(APITestCase):
    """Test cases for Workout API endpoints"""

    def setUp(self):
        """Set up test data"""
        self.workout_data = {
            'name': 'Morning Run',
            'description': 'A refreshing morning run',
            'difficulty_level': 'medium',
            'duration': 30,
            'target_audience': 'High School',
        }

    def test_create_workout(self):
        """Test creating a new workout"""
        response = self.client.post('/api/workouts/', self.workout_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], self.workout_data['name'])

    def test_list_workouts(self):
        """Test listing all workouts"""
        response = self.client.get('/api/workouts/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class APIRootTestCase(APITestCase):
    """Test cases for API root endpoint"""

    def test_api_root(self):
        """Test API root endpoint returns all endpoints"""
        response = self.client.get('/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('users', response.data)
        self.assertIn('teams', response.data)
        self.assertIn('activities', response.data)
        self.assertIn('leaderboard', response.data)
        self.assertIn('workouts', response.data)
