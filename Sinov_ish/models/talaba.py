from django.db import models
from django.contrib.auth.models import AbstractUser
from model_utils.fields import StatusField
from model_utils import Choices
from .fakultet import Fakultet




class Talaba(AbstractUser):
    STATUS = Choices('1', '2', '3', '4')
    kurs = StatusField()
    fakultet = models.ForeignKey('Fakultet', on_delete = models.CASCADE)
    img = models.ImageField(upload_to = 'user/',default=True)
    bio = models.CharField(max_length=100,default=True)