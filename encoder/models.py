from django.db import models

# Create your models here.
class images(models.Model):
    image_main = models.ImageField(upload_to='images/')
