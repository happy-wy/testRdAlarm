from django.db import models


# Create your models here.


class DevID(models.Model):
    devid = models.CharField(max_length=64, unique=True)
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.devid


class Image(models.Model):
    Aid = models.ForeignKey("DevID", to_field="devid", on_delete=models.CASCADE)
    type = models.CharField(max_length=64)
    time = models.BigIntegerField()
    speed = models.FloatField()
    picture = models.ImageField(upload_to='images/%Y/%m/%d')

    def __str__(self):
        s = "Alarm type :" + str(self.type)
        return s

    def __iter__(self):
        return self


class FileGz(models.Model):
    gz = models.FileField(upload_to='GzFile/%Y/%m/%d')

