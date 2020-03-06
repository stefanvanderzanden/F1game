from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


class GameProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    budget = models.IntegerField(default=1000000)
    jokers = models.IntegerField(default=2)
    cost = models.IntegerField(default=0)
    balance = models.IntegerField(default=1000000)


class RaceProfile(models.Model):
    driver1 = models.ForeignKey('game.Driver', on_delete=models.SET_NULL, related_name='race_profile_driver1',
                                null=True, blank=True)
    driver2 = models.ForeignKey('game.Driver', on_delete=models.SET_NULL, related_name='race_profile_driver2',
                                null=True, blank=True)
    team1 = models.ForeignKey('game.Team', on_delete=models.SET_NULL, related_name='race_profile_team1',
                              null=True, blank=True)
    team2 = models.ForeignKey('game.Team', on_delete=models.SET_NULL, related_name='race_profile_team2',
                              null=True, blank=True)

    joker_driver1 = models.BooleanField(default=False)
    joker_driver2 = models.BooleanField(default=False)
    joker_team1 = models.BooleanField(default=False)
    joker_team2 = models.BooleanField(default=False)
    fastest_driver = models.ForeignKey('game.Driver', blank=True, null=True,
                                       related_name='race_profile_fastest_driver', on_delete=models.SET_NULL)
    fastest_pit_stop = models.ForeignKey('game.Team', blank=True, null=True,
                                         related_name='race_profile_fastest_pit_stop', on_delete=models.SET_NULL)
    trivia_answer = models.ForeignKey('game.TriviaAnswer', related_name='race_profile_answer',
                                      on_delete=models.CASCADE)


class UserRaceResult(models.Model):
    race = models.ForeignKey('game.Race', related_name='user_race_results', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_race_results', on_delete=models.CASCADE)

    driver1 = models.ForeignKey('game.Driver', on_delete=models.SET_NULL,
                                related_name='race_result_driver1', null=True, blank=True)
    driver2 = models.ForeignKey('game.Driver', on_delete=models.SET_NULL,
                                related_name='race_result_driver2', null=True, blank=True)
    team1 = models.ForeignKey('game.Team', on_delete=models.SET_NULL,
                              related_name='race_result_team1', null=True, blank=True)
    team2 = models.ForeignKey('game.Team', related_name='race_result_team2',
                              on_delete=models.SET_NULL, null=True, blank=True)

    driver1_points_qualification = models.IntegerField(default=0)
    driver2_points_qualification = models.IntegerField(default=0)
    team1_points_qualification = models.IntegerField(default=0)
    team2_points_qualification = models.IntegerField(default=0)

    driver1_points_race = models.IntegerField(default=0)
    driver2_points_race = models.IntegerField(default=0)
    team1_points_race = models.IntegerField(default=0)
    team2_points_race = models.IntegerField(default=0)

    trivia_answer = models.ForeignKey('game.TriviaAnswer', related_name='race_result_answer',
                                      on_delete=models.CASCADE)

    fastest_driver = models.ForeignKey('game.Driver', blank=True, null=True,
                                       related_name='race_result_fastest_driver', on_delete=models.SET_NULL)
    fastest_pit_stop = models.ForeignKey('game.Team', blank=True, null=True,
                                         related_name='race_result_fastest_pit_stop', on_delete=models.SET_NULL)

    total_points_before = models.IntegerField(default=0, help_text='Total points before this race')
    total_points_after = models.IntegerField(default=0, help_text='Total points after this race, so race points '
                                                                  'and extra points in total')
    total_points_race = models.IntegerField(default=0, help_text='Points for drivers and teams')
    total_points_extra = models.IntegerField(default=0, help_text='Points for fastest questions and trivia')