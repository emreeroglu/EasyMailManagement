from django.db import models
from common.models import User


class EMailBox(models.Model):
    email = models.EmailField(blank=False, unique=True)
    mail_box_size = models.IntegerField(default=1)
    created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

    def __str__(self):
        if len(self.email):
            return self.email
        return self.email