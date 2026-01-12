from django.core.management.base import BaseCommand
from octofit_tracker.api.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Team.objects.all().delete()
        User.objects.all().delete()

        # Create users (super heroes)
        marvel_heroes = [
            {'username': 'ironman', 'email': 'ironman@marvel.com'},
            {'username': 'captainamerica', 'email': 'cap@marvel.com'},
            {'username': 'spiderman', 'email': 'spiderman@marvel.com'},
        ]
        dc_heroes = [
            {'username': 'batman', 'email': 'batman@dc.com'},
            {'username': 'superman', 'email': 'superman@dc.com'},
            {'username': 'wonderwoman', 'email': 'wonderwoman@dc.com'},
        ]
        marvel_users = [User.objects.create_user(**hero) for hero in marvel_heroes]
        dc_users = [User.objects.create_user(**hero) for hero in dc_heroes]

        # Create teams
        marvel_team = Team.objects.create(name='Marvel', members=marvel_users)
        dc_team = Team.objects.create(name='DC', members=dc_users)

        # Create activities
        for user in marvel_users + dc_users:
            Activity.objects.create(user=user, activity_type='run', duration=30, date=timezone.now().date())
            Activity.objects.create(user=user, activity_type='cycle', duration=45, date=timezone.now().date())

        # Create workouts
        for user in marvel_users + dc_users:
            Workout.objects.create(user=user, name='Pushups', description='Do 20 pushups', date=timezone.now().date())
            Workout.objects.create(user=user, name='Situps', description='Do 30 situps', date=timezone.now().date())

        # Create leaderboard
        Leaderboard.objects.create(team=marvel_team, score=200, week=1)
        Leaderboard.objects.create(team=dc_team, score=180, week=1)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
