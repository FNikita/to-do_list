from django.db import models

class itemLI(models.Model):
    check = models.BooleanField()
    text = models.TextField()

    def __str__(self):
        return self.text