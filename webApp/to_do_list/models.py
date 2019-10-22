from django.db import models

class ItemLi(models.Model):
    id = models.AutoField(primary_key=True)
    check = models.BooleanField(default=False)
    text = models.TextField()
    edit = models.BooleanField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text