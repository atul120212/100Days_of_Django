from django.db import models
# Create your models here.
from django.contrib.auth.models import User


class Receipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    receipe_name = models.CharField(max_length=200)
    receipe_description = models.TextField()
    receipe_image = models.ImageField(upload_to='receipe_images', blank=True)
