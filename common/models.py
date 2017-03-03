from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from uuid import uuid4


class User(AbstractUser):
    mobile = models.CharField(
        _("Mobile Phone"), blank=True, null=True, max_length=13
    )
    language = models.CharField(
        _("Language"), choices=settings.LANGUAGES, default='en', max_length=8
    )
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    @property
    def full_name(self):
        return ' '.join([str(self.first_name), str(self.last_name)])

    def __str__(self):
        if len(self.full_name):
            return self.full_name
        return self.username

    def save(self, *args, **kwargs):
        if not self.mobile:
            self.mobile = None
        if not self.username:
            self.username = str(uuid4())
        super(User, self).save(*args, **kwargs)

    class Meta:
        ordering = ('created_date',)
