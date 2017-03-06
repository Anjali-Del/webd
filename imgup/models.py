from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UploadModel(models.Model):
    username = models.CharField(max_length=128)
    image = models.ImageField(upload_to='db_images/')
