from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=13, null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
