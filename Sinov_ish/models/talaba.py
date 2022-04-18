from django.db import models
from django.contrib.auth.models import AbstractUser
from model_utils.fields import StatusField
from model_utils import Choices
from .fakultet import Fakultet




class Talaba(AbstractUser):
    fakultet = models.ForeignKey('Fakultet', on_delete = models.CASCADE,blank = True, null = True)
    img = models.ImageField(upload_to = 'user/',blank=True, null = True)
    bio = models.CharField(max_length=100,blank=True, null = True)
    STATUS = Choices('1', '2', '3', '4')
    kurs = StatusField()
    stipendiya = models.CharField(max_length=100, default="kiritilmagan", blank=True, null = True)

    def __str__(self):
        return self.username