# Generated by Django 3.1 on 2020-09-01 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0001_initial'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='difficultylevel',
            constraint=models.CheckConstraint(check=models.Q(('level__gte', 1), ('level__lte', 3)), name='level_between_1_and_3'),
        ),
    ]
