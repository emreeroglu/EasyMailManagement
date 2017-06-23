from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from EasyMailManagement.settings import DO_SERVER_REGION, DO_IMAGE_SLUG, DO_SIZE_SLUG, DO_SSH_KEY, DO_TAGS, DO_TOKEN, DO_NAME_PREFIX
from server.utils import DigitalOcean
from common.models import User


class Server(models.Model):
    name = models.CharField(blank=False, null=False, max_length=30)
    user = models.ForeignKey(User)
    ip_v4 = models.GenericIPAddressField(blank=True, null=True)
    ip_v6 = models.GenericIPAddressField(blank=True, null=True)
    ram_size = models.IntegerField(default=0)
    disk_size = models.IntegerField(default=0)
    cpu_count = models.IntegerField(default=0)
    is_available = models.BooleanField(default=True)
    static_mailbox_quota = models.IntegerField(default=0)
    is_ready = models.BooleanField(default=False)
    is_for_sell = models.BooleanField(default=False, blank=True)
    cpu_limit = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    ram_limit = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    disk_limit = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)

    def __str__(self):
        return self.name

    @classmethod
    def create(cls, droplet):
        server = None
        if droplet:
            ram_size = droplet.size_slug.strip('mb')
            server = cls(name=droplet.name, ip_v4=droplet.ip_address, ip_v6=droplet.ip_v6_address,
                         ram_size=ram_size, disk_size=droplet.disk, cpu_count=droplet.vcpus)
        return server

    def setup(self):
        droplet = DigitalOcean.create_droplet(token=DO_TOKEN, name=self.name, region=DO_SERVER_REGION, image=DO_IMAGE_SLUG, size_slug=DO_SIZE_SLUG, ssh_keys=DO_SSH_KEY, tags=DO_TAGS)
        server_list = DigitalOcean.get_droplet_list()
        list_size = len(server_list)
        # If new droplets status is not 'active' so it is 'new' wait until it turns to active
        # If server_list's size is same wait until get new server list
        while (droplet.status == 'new') or (list_size == len(server_list)):
            droplet.load()
            server_list = DigitalOcean.get_droplet_list()
        self.ip_v4 = droplet.ip_address
        self.ip_v6 = droplet.ip_v6_address
        self.ram_size = DO_SIZE_SLUG
        self.disk_size = droplet.disk
        self.cpu_count = droplet.vcpus
        self.save()
        # TODO I am not sure setting up OS called from here. This could be temporary

        return self

    # TODO This function will get parameters about new users and check available server in order to that information
    # TODO For example if there is not enough disk space on available server but cpu and ram new volume will be added
    @staticmethod
    def get_available_server():
        servers = Server.objects.all()
        latest_server_number = 0
        for server in servers:
            if server.is_available:
                # TODO check available server and return it if none of them is available create new one.
                # TODO decide availability parameters for a server
                # Taking latest server number for using in case of there is no available servers
                name = server.name
                latest_server_number_str = name.strip(DO_NAME_PREFIX)
                latest_server_number_int = int(latest_server_number_str)
                if latest_server_number_int > latest_server_number:
                    latest_server_number = latest_server_number_int
                return server
        latest_server_number += 1
        server_list = DigitalOcean.get_droplet_list()
        server_name = DO_NAME_PREFIX + str(latest_server_number)
        droplet = DigitalOcean.create_droplet(token=DO_TOKEN, name=server_name, region=DO_SERVER_REGION, image=DO_IMAGE_SLUG, size_slug=DO_SIZE_SLUG, ssh_keys=DO_SSH_KEY, tags=DO_TAGS)
        list_size = len(server_list)
        # If new droplets status is not 'active' so it is 'new' wait until it turns to active
        # If server_list's size is same wait until get new server list
        while (droplet.status == 'new') or (list_size == len(server_list)):
            droplet.load()
            server_list = DigitalOcean.get_droplet_list()
        server = Server.create(droplet)
        server.save()
        return server

    @staticmethod
    def set_email_box(email_box):
        server = Server.get_available_server()
        if server.is_ready:
            pass
        else:
            server.setup()
        server.add_email_box(email_box)

    def add_email_box(self):
        pass
