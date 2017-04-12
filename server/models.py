from django.db import models
from .commands import Debian


class Server(models.Model):
    name = models.CharField(blank=False, null=False, max_length=30)
    ip = models.GenericIPAddressField(blank=True, null=True)

    def find_available_server(self):
        pass

    def setup_server(self):
        debian = Debian()
        debian.ssh_copy_id()

