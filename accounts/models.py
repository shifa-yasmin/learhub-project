from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    class Role(models.TextChoices):
        STUDENT="student","Student"
        INSTRUCTOR="instructor","Instructor"
    role=models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.STUDENT,
    )
class UserProfile(models.Model):
    user=models.OneToOneField(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="profile"
    )  
    bio = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    profile_picture = models.URLField(blank=True)

    def __str__(self):
        return self.user.username      