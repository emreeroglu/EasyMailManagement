from django.db import models
from command.models import Command


class CommandSet(models.Model):
    name = models.CharField(blank=False, null=False, max_length=30)
    command = models.ManyToManyField(Command, blank=True, null=True)
    order = models.CharField(blank=True, null=True, max_length=1000)
