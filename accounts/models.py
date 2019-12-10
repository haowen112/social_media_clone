from django.db import models
from django.contrib.auth.models import User


# Create your models here.
def get_name(self):
    return "@{}".format(self.username)


User.add_to_class("__str__", get_name)
