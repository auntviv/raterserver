from django.db import models

class Game(models.Model):

    title = models.CharField(max_length=50)
    description = models.TextField()
    designer = models.CharField(max_length=50)
    year_released = models.IntegerField()
    number_of_players = models.IntegerField()
    number_of_players = models.IntegerField()
    age_recommendation = models.IntegerField()