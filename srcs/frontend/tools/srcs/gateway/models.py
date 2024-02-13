from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=30)

    def __str__(self):
        return (f"user id is {self.user_id}")