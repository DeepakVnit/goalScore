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
    team = models.ForeignKey(Teams, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0)])
    position = models.CharField(max_length=100, null=True)
    updated_at = models.DateTimeField(default=datetime.now)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name + " (" + self.team.name + ")"


class Matches(models.Model):
    id = models.AutoField(primary_key=True)
    team1 = models.ForeignKey(Teams, on_delete=models.CASCADE, related_name='team1')
    team2 = models.ForeignKey(Teams, on_delete=models.CASCADE, related_name='team2')
    score1 = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0)])
    score2 = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0)])
    penality1 = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0)])
    penality2 = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0)])
    venue = models.CharField(max_length=100, null=False)
    gametime = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.team1.name + " vs " + self.team2.name + " (" + str(datetime.date(self.gametime)) + ")"


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
    team = models.ForeignKey(Teams, on_delete=models.CASCADE, default=1)
    allowed = models.CharField(max_length=15, choices=GOAL_STATUS, default="Allowed")
    updated_at = models.DateTimeField(default=datetime.now)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.scorer.name


@receiver(signals.pre_save, sender=Goals)
def update_match_score(sender, instance, **kwargs):
    match_id = instance.match_id
    scorer_id = instance.scorer_id
    time = instance.time
    allowed = instance.allowed
    match_score = Matches.objects.filter(id=match_id)
    import pdb;
    pdb.set_trace()
    print("Receiver pre_save : {}- {} - {}: {}".format(match_id, scorer_id, match_score[0].team1.id,
                                                       match_score[0].team2.id))

    # check if Goal is already created
    goals = Goals.objects.filter(match_id=match_id, scorer_id=scorer_id, time=time)
    if allowed == 'Allowed':
        pass
    else:
        pass
