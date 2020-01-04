import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.shortcuts import reverse
from core import managers as core_managers
# Create your models here.


class User(AbstractUser):

    """Custom User MOdel"""

    LOGIN_EMAIL = "email"
    LOGIN_GITHUB = "github"
    LOGING_KAKAO = "kakao"

    LOGIN_CHOICES = (
        (LOGIN_EMAIL, "Email"),
        (LOGIN_GITHUB, "Github"),
        (LOGING_KAKAO, "Kakao"),
    )

    avatar = models.ImageField(upload_to="avatars", blank=True)
    bio = models.TextField(blank=True)
    zzigsa = models.BooleanField(default=False)
    login_method = models.CharField(
        max_length=50, choices=LOGIN_CHOICES, default=LOGIN_EMAIL
    )
    objects = core_managers.CustomUserManager()

    def get_absolute_url(self):
        return reverse("users:profile", kwargs={"pk": self.pk})
