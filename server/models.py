from django.db import models


class Server(models.Model):
    name = models.CharField(blank=False, null=False, max_length=30)
    operating_system = models.ForeignKey(OperatingSystem)


class OperatingSystem(models.Model):
    name = models.CharField(blank=False, null=False, max_length=30)


class CommandSet(models.Model):
    name = models.CharField(blank=False, null=False, max_length=30)
    operating_system = models.ForeignKey(OperatingSystem)


class Command(models.Model):
    name = models.CharField(blank=False, null=False, max_length=30)
    command = models.CharField(blank=False, null=False, max_length=1000)
    command_set = models.ForeignKey(CommandSet)
