from django.db import models

# Create your models here.

class appfamily(models.Model):
    name = models.CharField(max_length=30)
    birth_date = models.CharField(max_length=20)
    description = models.CharField(max_length=200, blank=True,null=True)
    active = models.BooleanField(default=True)