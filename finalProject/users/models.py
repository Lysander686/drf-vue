from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class CustomUser(AbstractUser, ):
    pass
