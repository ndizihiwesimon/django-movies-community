from datetime import datetime
from django.db import models

# Create your models here.
from django.db import models

from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin

# Create your models here.

Gender = (
    ('MALE', 'Male'),
    ('FEMALE', 'Female'),
    ('PREFER_NOT_SAY', 'Prefer Not to Say'),
)
class UserManager(BaseUserManager):
    def create_superuser(self, email, first_name, last_name, password, **other_fields):
        """Create and save a new superuser"""
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True')

        return self.create_user(email, first_name, last_name, password, **other_fields)

    def create_user(self, email, first_name, last_name, password=None, **other_fields):
        """Creates and saves a new User"""
        if not email:
            raise ValueError('User must have an email address')
        user = self.model(email=self.normalize_email(email), first_name=first_name,
                          last_name=last_name, **other_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user



class Member(AbstractBaseUser, PermissionsMixin):
    """Custom user model that support using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    gender =  models.CharField( max_length=100,choices=Gender,blank=False, null=False)
    dob = models.DateField(null=False, blank=False)
    telephone = models.CharField(max_length=20, blank=False, null=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
 

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    @property
    def age(self):
        return int((datetime.now().date() - self.birth_date).days / 365.25)

    def full_name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return self.full_name()