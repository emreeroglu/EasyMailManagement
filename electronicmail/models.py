from django.db import models
from multiprocessing import Process
from common.models import User
from server.models import Server


class ElectronicMail(models.Model):
    email = models.EmailField(blank=False, unique=True)
    mail_box_size = models.IntegerField(default=1)
    created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

    def __str__(self):
        if len(self.email):
            return self.email
        return self.email

    def setup(self):
        p = Process(target=Server.set_email_box, args=(self,))
        p.start()
        p.join()