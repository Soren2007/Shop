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

MODEL_NAME = "account"


GENDER_CHOICES = (
    (
        'True',
        _('مرد')
    ),
    (
        'False',
        _('زن')
    )
)


class CustomUserManager(BaseUserManager):
    """ Description """

    def create_user(
        self,
        phone_number,
        email="",
        first_name="",
        last_name="",
        is_active=False,
        password=None
    ):
        """ Description """
        if not phone_number:
            raise ValueError(_("Enter phone number"))
        if len(phone_number) < 11:
            raise ValueError(_('Invalid phone number'))
        user = self.model(
            phone_number=phone_number,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            is_active=is_active,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self,
        phone_number,
        email,
        first_name="",
        last_name="",
        password=None
    ):
        """ Description """
        user = self.create_user(
            mobile_number=phone_number,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,

        )
        user.is_completed = True
        user.is_active = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Address(models.Model):
    """ Description """
    uuid = models.UUIDField(
        unique=True,
        default=uuid4,
        editable=False,
        verbose_name=_('UUID')
    )

    address = models.TextField(
        verbose_name=_("Address"),
    )

    post_code = models.CharField(
        max_length=10,
        verbose_name=_("Post Code"),
        unique=True
    )

    longitude = models.CharField(
        max_length=10,
        verbose_name=_("Longitude"),
    )

    latitude = models.CharField(
        max_length=10,
        verbose_name=_("Latitude"),
    )
    
    create_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Create At")
    )
    
    update_at = models.DateTimeField(
        _("Update At"),
        auto_now = True
    )
    
    extra_data = models.JSONField(
        verbose_name=_("Extra Data"),
        null=True,
    )

    def __str__(self) -> str:
        return self.address

    class Meta:
        """ Description """
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'
        db_table = f"{MODEL_NAME}_addresses"


class User(AbstractBaseUser, PermissionsMixin):
    """ Description """
    uuid = models.UUIDField(
        unique=True,
        default=uuid4,
        editable=False,
        verbose_name=_('UUID')
    )

    phone_number = models.CharField(
        max_length=15,
        unique=True,
        verbose_name=_("Phone Number")
    )

    email = models.EmailField(
        max_length=200,
        verbose_name=_("Email"),
        null=True,
        blank=True,
        unique=True
    )

    first_name = models.CharField(
        max_length=50,
        verbose_name=_("First Name"),
        null=True,
        blank=True
    )

    last_name = models.CharField(
        max_length=50,
        verbose_name=_("Last Name"),
        null=True,
        blank=True
    )

    birthday = models.DateField(
        null=True,
        verbose_name=_("تاریخ تولد"),
        blank=True
    )

    gender = models.CharField(
        max_length=50,
        blank=True,
        choices=GENDER_CHOICES,
        default='True',
        null=True,
        verbose_name="Gender"
    )

    address = models.ManyToManyField(
        Address,
        verbose_name=_("Address"),
        null=True,
        blank=True
    )
    
    active_code = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name=_("Active Code"),
        editable=False
    )

    is_active = models.BooleanField(
        default=False,
        verbose_name=_("Is Active | n/y")
    )

    is_admin = models.BooleanField(
        default=False,
        verbose_name=_("Is Admin | n/y")
    )
    
    last_login_at = models.DateTimeField(
        default=timezone.now,
        verbose_name=_("Last Login At"),
        editable=False
    )

    create_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Create At")
    )
    
    update_at = models.DateTimeField(
        _("Update At"),
        auto_now = True
    )
    
    extra_data = models.JSONField(
        verbose_name=_("Extra Data"),
        null=True,
    )

    objects = CustomUserManager()

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    class Meta:
        """ Description """
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        db_table = f"{MODEL_NAME}_users"