from django.contrib.auth.models import AbstractUser
from django.db import models


# Add model User
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email")
    phone_number = models.CharField(
        max_length=30, blank=True, null=True, verbose_name="Phone number"
    )
    avatar = models.ImageField(
        upload_to="users/images/%Y/%m/%d/",
        default=None,
        null=True,
        blank=True,
        verbose_name="Saved user image",
    )
    country = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Country"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["email", "country"]

    def __str__(self):
        return self.email
