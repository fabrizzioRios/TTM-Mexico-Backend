from django.db import models


# Create your models here.

class Switch(models.Model):
    host_name = models.CharField(max_length=50)
