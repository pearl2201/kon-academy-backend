from django.db import models
from django.contrib.auth.models import AbstractUser

class KonUser(AbstractUser):
    def __str__(self):
        return self.email

# Create your models here.
class AssetPackage(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    asset = models.FileField(blank=True, default='')
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('KonUser', on_delete=models.CASCADE)
    price = models.IntegerField()

    def __str__(self):
        return self.title

class Lesson(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField()
    content = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('KonUser', on_delete=models.CASCADE)
    assets = models.ForeignKey('AssetPackage', on_delete=models.CASCADE)

    def __str__(self):
        return self.title