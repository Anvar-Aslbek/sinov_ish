from django.db import models
from .talaba import Talaba
from .fan import Fan

from model_utils.fields import StatusField
from model_utils import Choices


class Baho(models.Model):
    fan = models.ForeignKey('Fan',on_delete=models.CASCADE)
    user = models.ForeignKey('Talaba',on_delete=models.CASCADE)
    STATUS = Choices('2', '3', '4', '5')
    baho = StatusField()

    def __str__(self):
        return f"{self.user}ni {self.fan}idan bahosi {self.baho}"
