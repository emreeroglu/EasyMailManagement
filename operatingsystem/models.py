from django.db import models
from server.models import Server
from command.models import Command
from commandset.models import CommandSet


class OperatingSystem(models.Model):
    name = models.CharField(blank=False, null=False, max_length=30)
    server = models.ForeignKey(Server, blank=True, null=True)
    command = models.ForeignKey(Command, blank=True, null=True)
    command_set = models.ForeignKey(CommandSet, blank=True, null=True)