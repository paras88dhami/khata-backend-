from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, email, phone, full_name, password=None):
        if not email:
            raise ValueError("Email is required")
        if not phone:
            raise ValueError("Phone is required")

        email = self.normalize_email(email)

        user = self.model(
            email=email,
            phone=phone,
            full_name=full_name,
        )

        user.set_password(password) 
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone, full_name, password):
        user = self.create_user(email, phone, full_name, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["phone", "full_name"]

    def __str__(self):
        return self.email
