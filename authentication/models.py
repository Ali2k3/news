from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Author(AbstractUser):
    bio=models.TextField(max_length=2000)
