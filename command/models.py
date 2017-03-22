from django.db import models


class Command(models.Model):
    name = models.CharField(blank=False, null=False, max_length=30)
    command = models.CharField(blank=False, null=False, max_length=1000)