from digitalocean import Manager, Droplet
from digitalocean.baseapi import BaseAPI

from EasyMailManagement.settings import DO_TOKEN, DO_TAG


class DigitalOcean(object):
    @staticmethod
    def get_server_list():
        manager = Manager(token=DO_TOKEN)
        droplets = manager.get_all_droplets(tag_name=DO_TAG)
        return droplets

    @staticmethod
    def get_os_name_list():
        base_api = BaseAPI(token=DO_TOKEN)
        image_dict = base_api.get_data(url='images')
        image_list = image_dict.get('images')
        new_image_list = []
        for image in image_list:
            if image.get('slug') is not None:
                # if needed make image dictionary with only necessary pairs.
                new_image_list.append(image)
        return new_image_list

    @staticmethod
    def create_server(name=None, region=None, image_slug=None, size_slug=None, ssh_keys=[], backups=False):
        droplet = Droplet(token=DO_TOKEN, name=name, region=region, image=image_slug, size_slug=size_slug,
                          ssh_keys=ssh_keys, backups=backups)
        return droplet.create()
