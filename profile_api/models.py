from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager

# Create your models here.
class UserProfileManager(BaseUserManager):
    """Manager for user profile"""
    def create_user(self,email,first_name,last_name,password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')
        user = self.model(email=self.normalize_email(email),first_name=first_name,last_name=last_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,first_name,last_name,password):
        """Create and save a new superuser profile"""
        user = self.create_user(email,first_name,last_name,password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user





class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for user profile"""
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        """Return full name of user"""
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        """Return short name of user"""
        return f"{self.first_name}"

    def __str__(self):
        """Return string representation of user"""
        return self.email