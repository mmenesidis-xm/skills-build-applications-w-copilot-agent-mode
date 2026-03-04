from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from mongoengine.connection import get_db
from datetime import datetime

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear collections
        User.drop_collection()
        Team.drop_collection()
        Activity.drop_collection()
        Leaderboard.drop_collection()
        Workout.drop_collection()

        # Create teams
        marvel = Team(name='Marvel').save()
        dc = Team(name='DC').save()

        # Create users
        users = [
            User(name='Iron Man', email='ironman@marvel.com', team='Marvel').save(),
            User(name='Captain America', email='cap@marvel.com', team='Marvel').save(),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team='DC').save(),
            User(name='Batman', email='batman@dc.com', team='DC').save(),
        ]
        # Assign users to teams
        marvel.members = users[:2]
        marvel.save()
        dc.members = users[2:]
        dc.save()

        # Create activities
        Activity(user=users[0], type='Running', duration=30, date=datetime.now()).save()
        Activity(user=users[1], type='Cycling', duration=45, date=datetime.now()).save()
        Activity(user=users[2], type='Swimming', duration=60, date=datetime.now()).save()
        Activity(user=users[3], type='Yoga', duration=50, date=datetime.now()).save()

        # Create leaderboard
        Leaderboard(team=marvel, score=75).save()
        Leaderboard(team=dc, score=110).save()

        # Create workouts
        Workout(name='Morning Cardio', description='A quick morning cardio session', suggested_for=['Marvel', 'DC']).save()
        Workout(name='Strength Training', description='Build muscle strength', suggested_for=['Marvel']).save()
        Workout(name='Flexibility', description='Improve flexibility', suggested_for=['DC']).save()

        # Ensure unique index on email
        db = get_db()
        db.user.create_index('email', unique=True)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data!'))
