from django.test import TestCase
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class ModelSmokeTest(TestCase):
    def test_user_creation(self):
        user = User(name='Test User', email='test@example.com', team='Test').save()
        self.assertIsNotNone(user.id)
    def test_team_creation(self):
        team = Team(name='Test Team').save()
        self.assertIsNotNone(team.id)
    def test_activity_creation(self):
        user = User(name='Test User2', email='test2@example.com', team='Test').save()
        activity = Activity(user=user, type='Run', duration=10).save()
        self.assertIsNotNone(activity.id)
    def test_leaderboard_creation(self):
        team = Team(name='Test Team2').save()
        leaderboard = Leaderboard(team=team, score=100).save()
        self.assertIsNotNone(leaderboard.id)
    def test_workout_creation(self):
        workout = Workout(name='Test Workout', description='desc', suggested_for=['Test']).save()
        self.assertIsNotNone(workout.id)
