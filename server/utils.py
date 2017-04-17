from digitalocean import Manager, Droplet
from digitalocean.baseapi import BaseAPI

from EasyMailManagement.settings import DO_TOKEN, DO_TAGS


class DigitalOcean(object):
    @staticmethod
    def get_droplet_list():
        manager = Manager(token=DO_TOKEN)
        droplets = manager.get_all_droplets(tag_name=DO_TAGS)
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
    def create_droplet(*args, **kwargs):
        droplet = Droplet(*args, **kwargs)
        droplet.create()
        return droplet
