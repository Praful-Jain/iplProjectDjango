from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from ...models import Matches, Deliveries

import csv

class Command(BaseCommand):

    def import_matches(self):
        csv_file = 'matches.csv'
        with open(csv_file, 'r') as file:
            match_reader = csv.DictReader(file)
            for row in match_reader:
                # Create Matches instance and save it
                match_instance = Matches(
                    season  = int(row['season']),
                    city    = row['city'],
                    date    = row['date'],
                    team1   = row['team1'],
                    team2   = row['team2'],
                    toss_winner     = row['toss_winner'],
                    toss_decision   = row['toss_decision'],
                    result      = row['result'],
                    dl_applied  = int(row['dl_applied']),
                    winner      = row['winner'],
                    win_by_runs = int(row['win_by_runs']),
                    win_by_wickets  = int(row['win_by_wickets']),
                    player_of_match = row['player_of_match'],
                    venue   = row['venue'],
                    umpire1 = row['umpire1'],
                    umpire2 = row['umpire2'],
                    umpire3 = row['umpire3'],
                )
                match_instance.save()

    def import_deliveries(self):
        csv_file = 'deliveries.csv'
        with open(csv_file, 'r') as csv_file:
            dict_reader = csv.DictReader(csv_file)
            for row in dict_reader:
                try:
                    # Create a Matches instance first if needed
                    # For example, assuming your CSV contains match data as well
                    match_id_value = int(row['match_id'])
                    match_instance = Matches.objects.get(id=match_id_value)

                    # Create Deliveries instance
                    delivery_instance = Deliveries(
                        match_id     = match_instance,
                        inning       = int(row['inning']),
                        batting_team = row['batting_team'],
                        bowling_team = row['bowling_team'],
                        over    = int(row['over']),
                        ball    = int(row['ball']),
                        batsman = row['batsman'],
                        non_striker   = row['non_striker'],
                        bowler        = row['bowler'],
                        is_super_over = int(row['is_super_over']),
                        wide_runs     = int(row['wide_runs']),
                        bye_runs      = int(row['bye_runs']),
                        legbye_runs   = int(row['legbye_runs']),
                        noball_runs   = int(row['noball_runs']),
                        penalty_runs  = int(row['penalty_runs']),
                        batsman_runs  = int(row['batsman_runs']),
                        extra_runs    = int(row['extra_runs']),
                        total_runs    = int(row['total_runs']),
                        player_dismissed = row['player_dismissed'],
                        dismissal_kind   = row['dismissal_kind'],
                        fielder          = row['fielder'],
                    )
                    delivery_instance.save()
                except Matches.DoesNotExist:
                    # Handle the case where the Matches instance does not exist
                    self.stderr.write(self.style.ERROR(f'Matches with ID {match_id_value} does not exist.'))

    def handle(self, *args, **options):
        try:
            with transaction.atomic():
                self.import_matches()
                self.import_deliveries()
        except Exception as e:
            raise CommandError(f'An error occurred: {str(e)}')
