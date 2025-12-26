from enum import unique
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
     
    def create_user(self, email,password):

        if not email:
            raise ValueError('Email must require for the user')

        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)

        return user

        
    def create_superuser(self, email,password=None):

        user = self.create_user(email,password)
        
        user.is_staff=True
        user.is_superuser = True
        user.save(using = self._db)

        return user


class User(AbstractBaseUser,PermissionsMixin):

    email = models.EmailField(max_length=100, unique=True)
    first_name= models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

    objects=UserManager()

    class Meta:

        ordering = ('-created_at',)

    def __str__(self):

        return self.email