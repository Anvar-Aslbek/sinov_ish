from typing_extensions import Self
from django.db import models

from .fakultet import Fakultet


class Fan(models.Model):
    name = models.CharField(max_length=50)
    fakultet = models.ForeignKey('Fakultet', on_delete = models.CASCADE)


    def __str__(self):
        return self.name
