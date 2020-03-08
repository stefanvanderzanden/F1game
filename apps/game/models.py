from django.db import models
from django.utils.translation import ugettext_lazy as _


class Season(models.Model):
    year = models.IntegerField(help_text='The year the race started')
    active = models.BooleanField(default=False)

    def __str__(self):
        next_year = self.year + 1
        return 'Season for the year {0}-{1}'.format(self.year, next_year)


class Team(models.Model):
    name = models.CharField(max_length=120)
    value = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    season = models.ForeignKey('game.Season', related_name='teams', on_delete=models.CASCADE, null=True)
    order = models.IntegerField(help_text='Field to indicate the order of the teams')

    def __str__(self):
        return self.name


class Driver(models.Model):
    name = models.CharField(max_length=120)
    number = models.IntegerField()
    value = models.IntegerField()
    team = models.ForeignKey('game.Team', related_name='drivers', null=True, blank=True,
                             on_delete=models.SET_NULL)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    active = models.BooleanField(default=True,
                                 help_text='When a driver is not active for a race, this is to disable him')
    order = models.IntegerField(help_text='Field to indicate the order of the drivers within a team')
    season = models.ForeignKey('game.Season', related_name='drivers', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '{0} ({1})'.format(self.name, self.team.name)


class Race(models.Model):
    name = models.CharField(max_length=130)
    country = models.CharField(max_length=50)
    start = models.DateTimeField()
    description = models.TextField(null=True, blank=True)
    date_updated = models.DateTimeField()
    image = models.ImageField(null=True, blank=True)
    season = models.ForeignKey('game.Season', related_name='races', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '{0} ({1})'.format(self.name, self.season.year)


class ScoreTable(models.Model):
    """
    This is a model for storing the different scores for the different race types and different score types
    """
    DRIVER_OPTION = 'driver'
    MOTOR_OPTION = 'motor'

    SCORE_TYPE_OPTIONS = (
        (DRIVER_OPTION, _('Driver')),
        (MOTOR_OPTION, _('Motor'))
    )

    QUALIFICATION_CHOICE = 'qualification'
    RACE_CHOICE = 'race'
    RACE_TYPE_OPTIONS = (
        (QUALIFICATION_CHOICE, _('Qualification')),
        (RACE_CHOICE, _('Race'))
    )

    score_type = models.CharField(max_length=20, choices=SCORE_TYPE_OPTIONS)
    race_type = models.CharField(max_length=20, choices=RACE_TYPE_OPTIONS)
    result = models.IntegerField()
    points = models.IntegerField()
    extra_value = models.IntegerField()


class DriverResult(models.Model):
    driver = models.ForeignKey('game.Driver', related_name='results', on_delete=models.CASCADE)
    race = models.ForeignKey('game.Race', related_name='results', on_delete=models.CASCADE)
    result_qualification = models.IntegerField()
    result_race = models.IntegerField()
    fastest_lap = models.BooleanField(default=False)
    drive_through = models.BooleanField(default=False)

    class Meta:
        unique_together = ('driver', 'race')


class DriverProgress(models.Model):
    driver = models.ForeignKey('game.Driver', related_name='progresses', on_delete=models.CASCADE)
    race = models.ForeignKey('game.Race', related_name='driver_progresses', on_delete=models.CASCADE)
    start_value = models.IntegerField()
    end_value = models.IntegerField(null=True)


class TeamProgress(models.Model):
    Team = models.ForeignKey('game.Team', related_name='progresses', on_delete=models.CASCADE)
    race = models.ForeignKey('game.Race', related_name='team_progresses', on_delete=models.CASCADE)
    start_value = models.IntegerField()
    end_value = models.IntegerField(null=True)


class Trivia(models.Model):
    race = models.ForeignKey('game.Race', related_name='trivia', on_delete=models.SET_NULL, null=True, blank=True)
    question = models.CharField(max_length=128)  # TODO: make translatable


class TriviaAnswer(models.Model):
    trivia = models.ForeignKey('game.Trivia', related_name='answers', on_delete=models.CASCADE)
    answer = models.CharField(max_length=128)  # TODO: make translatable

