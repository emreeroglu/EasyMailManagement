from django.db import models
from server.models import Server


class OperatingSystem(models.Model):
    name = models.CharField(blank=False, null=False, max_length=30)
    server = models.ForeignKey(Server, blank=True, null=True)
