# Generated by Django 3.1 on 2020-08-28 15:54

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DifficultyLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)])),
            ],
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codename', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=256)),
                ('inspiration', models.CharField(max_length=256)),
                ('why', models.TextField()),
                ('what_if_not_achieved', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Subgoal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=256)),
                ('year', models.PositiveIntegerField()),
                ('difficulty_level', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='goals.difficultylevel')),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goals.goal')),
            ],
        ),
        migrations.AddField(
            model_name='difficultylevel',
            name='reward',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='goals.reward'),
        ),
    ]
