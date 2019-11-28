from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    """ Custom User Model """

    ZZIGSA_NOT_YET = "not yet"
    ZZIGSA_APPROVED = "approved"
    ZZIGSA_DENIED = "denied"

    ZZIGSA_CHOICES = (
        (ZZIGSA_NOT_YET, "Not yet"),
        (ZZIGSA_APPROVED, "Approved"),
        (ZZIGSA_DENIED, "Denied"),
    )

    nickname = models.CharField(max_length=20, unique=True)
    zzigsa = models.CharField(
        choices=ZZIGSA_CHOICES, max_length=10, default=ZZIGSA_DENIED
    )
