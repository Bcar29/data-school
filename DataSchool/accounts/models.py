from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager

# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self,email,password=None,**extra_fields):
        if not email:
            raise ValueError("l'email est obligatoire")
        user = self.model(email=self.normalize_email(email),**extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("le super utilisateur doit avoir is staff = True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("le super utilisateur doit avoir is superuser = True")
        
        return self.create_user(email, password, **extra_fields)


    

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True,blank=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = MyUserManager()

    def __str__(self):
        return self.email
    
