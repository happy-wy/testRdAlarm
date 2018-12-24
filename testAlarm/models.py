from django.db import models

# Create your models here.


class DevID(models.Model):
    devid = models.CharField(max_length=64)
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.devid