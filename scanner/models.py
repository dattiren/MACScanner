from django.db import models

# Create your models here.


class Organization(models.Model):
    registry = models.CharField(max_length=200, editable=False)
    assignment = models.CharField(max_length=20, editable=False)
    organization = models.CharField(max_length=200, editable=False)
    organization_address = models.CharField(max_length=1000, editable=False)


class Machine(models.Model):
    mac_address = models.CharField(max_length=20, editable=False)
    found_at = models.DateTimeField()
