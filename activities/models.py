from django.db import models


class Activity(models.Model):
    activity = models.CharField(max_length=100)
    accessibility = models.FloatField()
    type = models.CharField(max_length=100)
    participants = models.IntegerField()
    price = models.FloatField()
    link = models.CharField(max_length=100)

    def __str__(self):
        return self.activity
