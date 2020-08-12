from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    avatar = models.FileField(upload_to='users/', blank=True, null=True)

    def __str__(self):
        return self.username
