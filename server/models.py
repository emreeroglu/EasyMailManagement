from django.db import models


class Server(models.Model):
    name = models.CharField(blank=False, null=False, max_length=30)
    ip = models.GenericIPAddressField(blank=True, null=True)
