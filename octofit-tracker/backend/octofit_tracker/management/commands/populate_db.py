from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data.'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Users
        user1 = User.objects.create(username='alice', email='alice@example.com', password='password1')
        user2 = User.objects.create(username='bob', email='bob@example.com', password='password2')
        user3 = User.objects.create(username='carol', email='carol@example.com', password='password3')

        # Teams
        team1 = Team.objects.create(name='Team Alpha')
        team1.members.add(user1, user2)
        team2 = Team.objects.create(name='Team Beta')
        team2.members.add(user3)

        # Activities
        Activity.objects.create(user=user1, activity_type='Running', duration=timedelta(hours=1))
        Activity.objects.create(user=user2, activity_type='Cycling', duration=timedelta(minutes=45))
        Activity.objects.create(user=user3, activity_type='Swimming', duration=timedelta(minutes=30))

        # Leaderboard
        Leaderboard.objects.create(user=user1, score=120)
        Leaderboard.objects.create(user=user2, score=100)
        Leaderboard.objects.create(user=user3, score=80)

        # Workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups')
        Workout.objects.create(name='Situps', description='Do 30 situps')
        Workout.objects.create(name='Jump Rope', description='Jump rope for 10 minutes')

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
