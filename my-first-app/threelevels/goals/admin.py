from django.contrib import admin

from .models import Goal, Subgoal, DifficultyLevel, Reward

admin.site.register(Goal)
admin.site.register(Subgoal)
admin.site.register(DifficultyLevel)
admin.site.register(Reward)