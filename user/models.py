from django.db import models

# Create your models here.


class User(models.Model):
    class AdminUserChoices(models.IntegerChoices):
        ADMIN = 1
        CLIENT = 0

    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=13, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    admin_user = models.IntegerField(choices=AdminUserChoices, default=0)

    def is_admin(self):
        if hasattr(self, "admin_user") == 1:
            return True
        else:
            return False

    def is_client(self):
        if hasattr(self, "admin_user") == 0:
            return True
        else:
            return False
