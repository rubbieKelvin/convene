# from authentication.managers import UserManager
from django.db import models
from django.contrib.auth.models import AbstractUser

from uuid import uuid4
from apps.main.managers.user import UserManager


class User(AbstractUser):
	username = None

	id = models.UUIDField(
        default=uuid4,
        unique=True,
        editable=False,
        primary_key=True)

	email = models.EmailField(
        unique=True,
        max_length=225)

	first_name = models.CharField(
        max_length=30,
        null=False,
        blank=False)

	last_name = models.CharField(
        max_length=30,
        null=False,
        blank=False)
    
	phone = models.CharField(
        unique=True,
        default=None,
        null=True,
        blank=True,
        max_length=16)

	secondary_phone = models.CharField(
        default=None,
        blank=True,
        max_length=16,
        null=True)

	photo = models.ImageField(
        null=True,
        blank=True,
        max_length=5000)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['first_name', 'last_name']

	objects = UserManager()

	def __str__(self) -> str:
		return self.email

	def __repr__(self) -> str:
		return f"<User {self.email}>"

	@property
	def fullname(self) -> str:
		return f"{self.first_name} {self.last_name}"
