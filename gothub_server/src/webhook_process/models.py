from django.contrib.auth.models import AbstractUser
from django.db import models


# class User(AbstractUser):
#     github_token = models.CharField(max_length=800, null=True, blank=True)
#     github_installation_id = models.IntegerField(null=True, blank=True)
#     token_expires_at = models.DateTimeField(null=True, blank=True)
#     github_username = models.CharField(max_length=300, null=True, blank=True)
