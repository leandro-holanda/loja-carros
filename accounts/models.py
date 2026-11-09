from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    cpf = models.CharField(max_length=11, unique=True)
    city = models.CharField(max_length=100)
    neighborhood = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username