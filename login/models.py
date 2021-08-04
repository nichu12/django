from django.db import models

# Create your models here.
class Login(models.Model):
    phone = models.IntegerField()
    email = models.CharField(max_length=100)
    website = models.CharField(max_length=100)