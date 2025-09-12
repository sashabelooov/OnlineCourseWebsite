from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    fio = models.CharField(max_length=255, blank=True, null=True)

    profile_image = models.ImageField(
        upload_to='profile_images/',          # images/profile_images/ ichida saqlanadi
        blank=True,
        null=True
    )

    coins = models.PositiveIntegerField(default=0)

    ROLE_CHOICES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('superuser', 'Superuser'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f"{self.email} ({self.role})"
