from django.db import models

class itemLI(models.Model):

    check = models.BooleanField()
    text = models.TextField()
    edit = models.BooleanField(default=0)
    deleted = models.BooleanField(default=0)

    def __str__(self):
        return self.text