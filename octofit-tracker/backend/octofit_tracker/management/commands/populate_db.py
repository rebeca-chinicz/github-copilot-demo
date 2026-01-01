"""
Django management command to populate the octofit_db database with test data.

This command initializes the database with sample users, teams, activities, 
leaderboard entries, and workouts for testing the OctoFit Tracker application.
"""
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone
from datetime import timedelta


class Command(BaseCommand):
    """Management command to populate the database with test data"""
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        """Execute the command to populate test data"""
        # Clear existing data
        self.stdout.write(self.style.WARNING('Clearing existing data...'))
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create test users - Superhero themed for Mergington High School
        self.stdout.write(self.style.SUCCESS('Creating test users...'))
        users_data = [
            {
                'username': 'captain_fitness',
                'email': 'captain@mergington.edu',
                'password': 'CaptainPass123!',
            },
            {
                'username': 'iron_runner',
                'email': 'iron@mergington.edu',
                'password': 'IronPass123!',
            },
            {
                'username': 'spider_trainer',
                'email': 'spider@mergington.edu',
                'password': 'SpiderPass123!',
            },
            {
                'username': 'black_panther_fit',
                'email': 'panther@mergington.edu',
                'password': 'PantherPass123!',
            },
            {
                'username': 'thunder_athlete',
                'email': 'thunder@mergington.edu',
                'password': 'ThunderPass123!',
            },
        ]

        users = []
        for user_data in users_data:
            user = User.objects.create(**user_data)
            users.append(user)
            self.stdout.write(f'  Created user: {user.username}')

        # Create test teams
        self.stdout.write(self.style.SUCCESS('Creating test teams...'))
        teams_data = [
            {
                'name': 'Mergington Warriors',
                'description': 'The elite fitness team of Mergington High School',
            },
            {
                'name': 'PE Champions',
                'description': 'Champions of physical education and athletic excellence',
            },
            {
                'name': 'Cardio Kings',
                'description': 'Focused on cardiovascular fitness and endurance',
            },
        ]

        teams = []
        for team_data in teams_data:
            team = Team.objects.create(**team_data)
            teams.append(team)
            self.stdout.write(f'  Created team: {team.name}')

        # Create test activities
        self.stdout.write(self.style.SUCCESS('Creating test activities...'))
        activities_data = [
            {
                'user': users[0],
                'activity_type': 'running',
                'duration': 45,
                'distance': 7.5,
                'calories': 675,
            },
            {
                'user': users[0],
                'activity_type': 'cycling',
                'duration': 60,
                'distance': 25.0,
                'calories': 600,
            },
            {
                'user': users[1],
                'activity_type': 'weight_training',
                'duration': 90,
                'distance': None,
                'calories': 800,
            },
            {
                'user': users[1],
                'activity_type': 'swimming',
                'duration': 60,
                'distance': 2.0,
                'calories': 700,
            },
            {
                'user': users[2],
                'activity_type': 'yoga',
                'duration': 45,
                'distance': None,
                'calories': 200,
            },
            {
                'user': users[2],
                'activity_type': 'hiking',
                'duration': 120,
                'distance': 8.0,
                'calories': 900,
            },
            {
                'user': users[3],
                'activity_type': 'basketball',
                'duration': 90,
                'distance': None,
                'calories': 750,
            },
            {
                'user': users[3],
                'activity_type': 'running',
                'duration': 30,
                'distance': 5.0,
                'calories': 450,
            },
            {
                'user': users[4],
                'activity_type': 'volleyball',
                'duration': 60,
                'distance': None,
                'calories': 400,
            },
            {
                'user': users[4],
                'activity_type': 'running',
                'duration': 50,
                'distance': 8.0,
                'calories': 700,
            },
        ]

        activities = []
        for activity_data in activities_data:
            activity = Activity.objects.create(**activity_data)
            activities.append(activity)
            self.stdout.write(
                f'  Created activity: {activity.user.username} - {activity.activity_type}'
            )

        # Create leaderboard entries
        self.stdout.write(self.style.SUCCESS('Creating leaderboard entries...'))
        leaderboard_data = [
            {
                'user': users[0],
                'score': 2750,
                'rank': 1,
                'total_activities': 2,
                'total_duration': 105,
            },
            {
                'user': users[1],
                'score': 2500,
                'rank': 2,
                'total_activities': 2,
                'total_duration': 150,
            },
            {
                'user': users[2],
                'score': 2100,
                'rank': 3,
                'total_activities': 2,
                'total_duration': 165,
            },
            {
                'user': users[3],
                'score': 2400,
                'rank': 4,
                'total_activities': 2,
                'total_duration': 120,
            },
            {
                'user': users[4],
                'score': 2100,
                'rank': 5,
                'total_activities': 2,
                'total_duration': 110,
            },
        ]

        leaderboards = []
        for lb_data in leaderboard_data:
            leaderboard = Leaderboard.objects.create(**lb_data)
            leaderboards.append(leaderboard)
            self.stdout.write(
                f'  Created leaderboard: {leaderboard.user.username} - Rank: {leaderboard.rank}'
            )

        # Create test workouts
        self.stdout.write(self.style.SUCCESS('Creating test workouts...'))
        workouts_data = [
            {
                'name': 'Morning Power Run',
                'description': 'High-intensity 5K run to start your day with energy',
                'difficulty_level': 'medium',
                'duration': 30,
                'target_audience': 'High School Students',
            },
            {
                'name': 'Full Body Strength',
                'description': 'Complete strength training routine targeting all major muscle groups',
                'difficulty_level': 'hard',
                'duration': 90,
                'target_audience': 'All Levels',
            },
            {
                'name': 'Cardio Blast',
                'description': 'Heart-pumping cardio workout combining running and jumping',
                'difficulty_level': 'hard',
                'duration': 45,
                'target_audience': 'Intermediate',
            },
            {
                'name': 'Yoga Flow',
                'description': 'Relaxing yoga session for flexibility and mental clarity',
                'difficulty_level': 'easy',
                'duration': 45,
                'target_audience': 'Beginners',
            },
            {
                'name': 'Basketball Conditioning',
                'description': 'Sport-specific drills to improve basketball performance',
                'difficulty_level': 'medium',
                'duration': 60,
                'target_audience': 'Basketball Players',
            },
            {
                'name': 'Swimming Intervals',
                'description': 'Interval-based swimming workout to build endurance',
                'difficulty_level': 'hard',
                'duration': 60,
                'target_audience': 'Swimmers',
            },
            {
                'name': 'Beginner Fitness',
                'description': 'Gentle workout perfect for those just starting their fitness journey',
                'difficulty_level': 'easy',
                'duration': 30,
                'target_audience': 'Beginners',
            },
            {
                'name': 'HIIT Challenge',
                'description': 'High-Intensity Interval Training for maximum calorie burn',
                'difficulty_level': 'hard',
                'duration': 30,
                'target_audience': 'Advanced',
            },
        ]

        workouts = []
        for workout_data in workouts_data:
            workout = Workout.objects.create(**workout_data)
            workouts.append(workout)
            self.stdout.write(
                f'  Created workout: {workout.name} ({workout.difficulty_level})'
            )

        self.stdout.write(
            self.style.SUCCESS(
                f'\n✓ Successfully populated database with test data!\n'
                f'  Created: {len(users)} users\n'
                f'  Created: {len(teams)} teams\n'
                f'  Created: {len(activities)} activities\n'
                f'  Created: {len(leaderboards)} leaderboard entries\n'
                f'  Created: {len(workouts)} workouts'
            )
        )
