from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.conf import settings

from django.db.models import Q
from PIL import Image
from .validators import ASCIIUsernameValidator

FATHER = "Father"
MOTHER = "Mother"
OTHER = "Other"

RELATION_SHIP = (
    (FATHER, "Father"),
    (MOTHER, "Mother"),
    (OTHER, "Other"),
)


class CustomUserManager(UserManager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(username__icontains=query) |
                         Q(first_name__icontains=query) |
                         Q(last_name__icontains=query) |
                         Q(email__icontains=query)
                         )
            qs = qs.filter(or_lookup).distinct()  # distinct() is often necessary with Q lookups
        return qs


class Account(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_parent = models.BooleanField(default=False)
    phone = models.CharField(max_length=60, blank=True, null=True)
    address = models.CharField(max_length=60, blank=True, null=True)
    picture = models.ImageField(upload_to='profile_pictures/%y/%m/%d/', default='default.png', null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    admin = models.BooleanField(default=False)
    class Meta:
        unique_together = []
    username_validator = ASCIIUsernameValidator()

    # Remove the unique constraint from the username field
    username = models.CharField(
        max_length=150,
        unique=True,  # Remove the unique constraint
        validators=[username_validator],
        error_messages={
            'unique': "A user with that username already exists.",
        }
    )

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    # Rest of your User model remains the same
