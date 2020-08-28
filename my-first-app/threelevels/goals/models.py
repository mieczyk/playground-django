from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Goal(models.Model):
    codename = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    inspiration = models.CharField(max_length=256)
    why = models.TextField()
    what_if_not_achieved = models.TextField()

class Reward(models.Model):
    name = models.CharField(max_length=256)

class DifficultyLevel(models.Model):
    level = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(3)]
    )
    reward = models.ForeignKey(Reward, null=True, on_delete=models.SET_NULL)

class Subgoal(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    description = models.CharField(max_length=256)
    difficulty_level = models.ForeignKey(DifficultyLevel, on_delete=models.PROTECT)
    year = models.PositiveIntegerField()

