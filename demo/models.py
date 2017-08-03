from django.db import models


class MyThing(models.Model):
    description = models.CharField(max_length=100)
