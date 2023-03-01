from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=20)
    stat = models.BooleanField()
