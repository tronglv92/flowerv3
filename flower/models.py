from django.db import models


class Hoa(models.Model):
    name = models.CharField(max_length=250)
    number = models.IntegerField(default=0)
