from django.db import models

class Image(models.Model):
    
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    player = models.ForeignKey("Player", on_delete=models.CASCADE)
    image_url = models.CharField(max_length=55)