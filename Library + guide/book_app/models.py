from django.db import models
from django.contrib.auth.models import User
import datetime

#Previously Author
class Diet(models.Model):
    writer = (
        ('intermittent fasting','intermittent fasting'),
        ('Atkins diet','Atkins diet'),
        ('Ketogenic diet','Ketogenic diet'),
        ('South Beach diet','South Beach diet'),
        ('Weight Watchers diet','Weight Watchers diet'),
        ("Mediterranean diet","Mediterranean diet")
    )
    available_diets = models.CharField(max_length = 200, choices = writer, blank = True, unique=True)

    def __str__(self):
        return self.available_diets

#Previously Book
class Soft75(models.Model):
    Workout = models.PositiveIntegerField(default=1)
    Water = models.PositiveIntegerField(default=0)
    Skill = models.PositiveIntegerField(default=0)
    def __str__(self):
        return "%s %s" % (self.Workout, self.Water, self.Skill )
