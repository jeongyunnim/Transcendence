from django.db import models

# Create your models here.

class LoginData(models.Model):
    id = models.CharField(max_length=30)
    password = models.CharField(max_length=30)