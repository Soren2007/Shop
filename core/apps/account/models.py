from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin
)
from uuid import uuid4

# Create your models here.


class CustomUserManager(BaseUserManager):
    """ Description """

    def create_user(
        self,
        mobile_number,
        email="",
        name="",
        family="",
        is_active=False,
        password=None
    ):
        """ Description """
        if not mobile_number:
            raise ValueError(_("شماره موبایل باید وارد شود"))
        if len(mobile_number) < 11:
            raise ValueError(_('شماره موبایل وارد شده صحیح نمی باشد.'))
        user = self.model(
            mobile_number=mobile_number,
            email=self.normalize_email(email),
            name=name,
            family=family,
            is_active=is_active,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self,
        mobile_number,
        email,
        name,
        family,
        password=None
    ):
        """ Description """
        user = self.create_user(
            mobile_number=mobile_number,
            email=email,
            name=name,
            family=family,
            password=password,

        )
        user.is_completed = True
        user.is_active = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


