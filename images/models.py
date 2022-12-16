from django.db import models

# Create your models here.
class Image(models.Model):
    prompt = models.CharField(max_length=500)
    number = models.IntegerField(default=1)
    url = models.CharField(max_length=2000)
    likes = models.IntegerField(default=0)
    resolution = models.CharField(max_length=100, choices=[('small','256x256'), ('medium','512x512'), ('large','1024x1024')])

    class Meta:
        ordering = ["id"]