import uuid
from datetime import datetime

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import signals
from django.dispatch import receiver


def change_file_name(instance, filename):
    extension = filename.split('.')[-1]
    return '{0}.{1}'.format(uuid.uuid4(), extension)


class Teams(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    short_name = models.CharField(max_length=100, null=False)
    flag = models.ImageField(upload_to=change_file_name, null=True)
    group = models.CharField(max_length=2, null=False)
    updated_at = models.DateTimeField(default=datetime.now)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name


class Players(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    age = models.IntegerField(default=0)
    team = models.ForeignKey(Teams, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0)])
    position = models.CharField(max_length=100, null=True)
    updated_at = models.DateTimeField(default=datetime.now)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name + " (" + self.team.name + ")"


class Matches(models.Model):
    POSSIBLE_RESULT = (('WON', 'WON'), ('LOST', 'LOST'), ('DRAW', 'DRAW'))
    MATCH_STATUS = (('LIVE', 'LIVE'), ('HALF TIME', 'HALF TIME'), ('FULL TIME', 'FULL TIME'))
    id = models.AutoField(primary_key=True)
    team1 = models.ForeignKey(Teams, on_delete=models.CASCADE, related_name='team1')
    team2 = models.ForeignKey(Teams, on_delete=models.CASCADE, related_name='team2')
    captain_team1 = models.ForeignKey(Players, on_delete=models.CASCADE, related_name='Captain_team1')
    captain_team2 = models.ForeignKey(Players, on_delete=models.CASCADE, related_name='Captain_team2')
    score1 = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0)])
    score2 = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0)])
    penality1 = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0)])
    penality2 = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0)])
    venue = models.CharField(max_length=100, null=False)
    status = models.CharField(max_length=20, choices=MATCH_STATUS, default=None)
    result = models.CharField(max_length=100, choices=POSSIBLE_RESULT, default=" ")
    gametime = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.team1.name + " vs " + self.team2.name + " (" + str(datetime.date(self.gametime)) + ")"


class Cards(models.Model):
    CARD_TYPE = (
        ('Yellow', 'Yellow'),
        ('Red', 'Red'),
    )
    id = models.AutoField(primary_key=True)
    match = models.ForeignKey(Matches, on_delete=models.CASCADE, related_name='match')
    card_type = models.CharField(max_length=15, choices=CARD_TYPE, default="Yellow")
    player = models.ForeignKey(Players, on_delete=models.CASCADE, related_name='player')
    time = models.IntegerField(default=0, validators=[MaxValueValidator(140), MinValueValidator(0)])
    updated_at = models.DateTimeField(default=datetime.now)
    created_at = models.DateTimeField(default=datetime.now)


class Goals(models.Model):
    GOAL_STATUS = (
        ('Allowed', 'Allowed'),
        ('DisAllowed', 'DisAllowed'),
    )

    id = models.AutoField(primary_key=True)
    scorer = models.ForeignKey(Players, on_delete=models.CASCADE, related_name='scorer')
    assist = models.ForeignKey(Players, on_delete=models.CASCADE, related_name='assist')
    time = models.IntegerField(default=0, validators=[MaxValueValidator(140), MinValueValidator(0)])
    match = models.ForeignKey(Matches, on_delete=models.CASCADE, default=1)
    awarded_team = models.ForeignKey(Teams, on_delete=models.CASCADE, default=1)
    is_penalty = models.BooleanField(default=False)
    allowed = models.CharField(max_length=15, choices=GOAL_STATUS, default="Allowed")
    owngoal = models.BooleanField(default=False)
    updated_at = models.DateTimeField(default=datetime.now)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.scorer.name


@receiver(signals.post_save, sender=Goals)
def create_goal_update_score(sender, instance, **kwargs):
    match_id = instance.match_id
    allowed = instance.allowed
    team = instance.awarded_team
    match_score = Matches.objects.get(id=match_id)

    if allowed == 'Allowed' and kwargs['created']:
        if team.name == match_score.team1.name:
            match_score.score1 += 1
        elif team.name == match_score.team2.name:
            match_score.score2 += 1
        match_score.save()