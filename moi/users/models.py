from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete =  models.CASCADE,
        primary_key = True
    )

    experience = models.PositiveBigIntegerField()

    def __str__(self):
        return self.user.username
