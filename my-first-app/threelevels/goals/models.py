from django.db import models
from django.db.models import Q
from django.core.validators import MaxValueValidator, MinValueValidator

class Goal(models.Model):
    codename = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    inspiration = models.CharField(max_length=256)
    why = models.TextField()
    what_if_not_achieved = models.TextField()

    def __str__(self):
        return '[{}] {}'.format(self.codename, self.description)

class Reward(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class DifficultyLevel(models.Model):
    level = models.PositiveSmallIntegerField(
        # The validators are run only if ModelForm is used.
        # They will not run before saving the model in DB.
        validators=[MinValueValidator(1), MaxValueValidator(3)]
    )
    reward = models.ForeignKey(Reward, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.level)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=Q(level__gte=1, level__lte=3), name='level_between_1_and_3'
            )
        ]

class Subgoal(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    description = models.CharField(max_length=256)
    difficulty_level = models.ForeignKey(DifficultyLevel, on_delete=models.PROTECT)
    year = models.PositiveIntegerField()

    def __str__(self):
        return self.description

