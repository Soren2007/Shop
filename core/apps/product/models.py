from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
from apps.search.models import Tag
from uuid import uuid4
# Create your models here.


MODEL_NAME = "product"


class Brand(models.Model):
    uuid = models.UUIDField(
        unique=True,
        default=uuid4,
        editable=False,
        verbose_name=_('UUID')
    )

    name = models.CharField(
        max_length=100,
        verbose_name=_('Name'),
        unique=True
    )

    logo = models.ImageField(
        upload_to='brands/',
        verbose_name=_('Logo'),
    )

    about = RichTextField(
        verbose_name=_("About"),
        blank=True,
        null=True,
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

    def __str__(self):
        return self.user

    class Meta:
        """ Description """
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'
        db_table = f"{MODEL_NAME}_brands"


class Category(models.Model):
    uuid = models.UUIDField(
        unique=True,
        default=uuid4,
        editable=False,
        verbose_name=_('UUID')
    )

    name = models.CharField(
        max_length=100,
        verbose_name=_('Name'),
        unique=True
    )

    image = models.ImageField(
        upload_to='brands/',
        verbose_name=_('Image'),
    )

    tags = models.ManyToManyField(
        Tag,
        verbose_name=_('Tags'),
        blank=True,
    )

    visits = models.PositiveIntegerField(
        default=0,
        verbose_name=_('Visits'),
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

    def __str__(self):
        return self.name

    class Meta:
        """ Description """
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        db_table = f"{MODEL_NAME}_categories"


class ProductImage(models.Model):
    uuid = models.UUIDField(
        unique=True,
        default=uuid4,
        editable=False,
        verbose_name=_('UUID')
    )

    name = models.CharField(
        max_length=100,
        verbose_name=_("Name")
    )

    image = models.ImageField(
        verbose_name=_("Image"),
        upload_to="",
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
    def __str__(self):
        return self.name

    class Meta:
        """ Description """
        verbose_name = _('Product Image')
        verbose_name_plural = _('Product Images')
        db_table = f"{MODEL_NAME}_product_images"

class Product(models.Model):
    uuid = models.UUIDField(
        unique=True,
        default=uuid4,
        editable=False,
        verbose_name=_('UUID')
    )

    name = models.CharField(
        max_length=150,
        verbose_name=_("Name")
    )

    price = models.PositiveIntegerField(
        verbose_name=_("Price"),
    )

    rating = models.PositiveIntegerField(
        verbose_name=_("Rating"),
    )

    tags = models.ManyToManyField(
        Tag,
        verbose_name=_('Tags'),
        blank=True,
    )

    brand = models.ForeignKey(
        verbose_name=_("Brand"),
        on_delete=models.CASCADE,
    )


    category = models.ManyToManyField(
        verbose_name=_("Category"),
    )


    product_images = models.ManyToManyField(
        ProductImage,
        verbose_name=_("Product Images"),
        blank=True,
    )

    description = RichTextField(
        verbose_name=_("Description"),
        blank=True,
        null=True,
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
    def __str__(self):
        return self.name

    class Meta:
        """ Description """
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
        db_table = f"{MODEL_NAME}_products"