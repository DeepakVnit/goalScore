# Generated by Django 2.0.6 on 2018-06-15 15:25

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import goalScoreApp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('card_type', models.CharField(choices=[('Yellow', 'Yellow'), ('Red', 'Red')], default='Yellow', max_length=15)),
                ('time', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(140), django.core.validators.MinValueValidator(0)])),
                ('updated_at', models.DateTimeField(default=datetime.datetime.now)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Goals',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('time', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(140), django.core.validators.MinValueValidator(0)])),
                ('allowed', models.CharField(choices=[('Allowed', 'Allowed'), ('DisAllowed', 'DisAllowed')], default='Allowed', max_length=15)),
                ('updated_at', models.DateTimeField(default=datetime.datetime.now)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Matches',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('score1', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)])),
                ('score2', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)])),
                ('penality1', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)])),
                ('penality2', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)])),
                ('venue', models.CharField(max_length=100)),
                ('result', models.CharField(choices=[('WON', 'WON'), ('LOST', 'LOST'), ('DRAW', 'DRAW')], default=' ', max_length=100)),
                ('gametime', models.DateTimeField(default=datetime.datetime.now)),
                ('updated_at', models.DateTimeField(default=datetime.datetime.now)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField(default=0)),
                ('rating', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)])),
                ('position', models.CharField(max_length=100, null=True)),
                ('updated_at', models.DateTimeField(default=datetime.datetime.now)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('short_name', models.CharField(max_length=100)),
                ('flag', models.ImageField(null=True, upload_to=goalScoreApp.models.change_file_name)),
                ('group', models.CharField(max_length=2)),
                ('updated_at', models.DateTimeField(default=datetime.datetime.now)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.AddField(
            model_name='players',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goalScoreApp.Teams'),
        ),
        migrations.AddField(
            model_name='matches',
            name='captain_team1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Captain_team1', to='goalScoreApp.Players'),
        ),
        migrations.AddField(
            model_name='matches',
            name='captain_team2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Captain_team2', to='goalScoreApp.Players'),
        ),
        migrations.AddField(
            model_name='matches',
            name='team1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team1', to='goalScoreApp.Teams'),
        ),
        migrations.AddField(
            model_name='matches',
            name='team2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team2', to='goalScoreApp.Teams'),
        ),
        migrations.AddField(
            model_name='goals',
            name='assist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assist', to='goalScoreApp.Players'),
        ),
        migrations.AddField(
            model_name='goals',
            name='match',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='goalScoreApp.Matches'),
        ),
        migrations.AddField(
            model_name='goals',
            name='scorer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scorer', to='goalScoreApp.Players'),
        ),
        migrations.AddField(
            model_name='goals',
            name='team',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='goalScoreApp.Teams'),
        ),
        migrations.AddField(
            model_name='cards',
            name='match',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match', to='goalScoreApp.Matches'),
        ),
        migrations.AddField(
            model_name='cards',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player', to='goalScoreApp.Players'),
        ),
    ]
