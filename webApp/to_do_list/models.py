from django.db import models

class itemLI(models.Model):
    check = models.BooleanField()
    text = models.TextField()
