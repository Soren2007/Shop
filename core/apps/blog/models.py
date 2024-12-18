from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from apps.account.models import User
from apps.search.models import Tag
from ckeditor.fields import RichTextField
from uuid import uuid4



# Create your models here.



MODEL_NAME = "blog"


class Article(models.Model):
    uuid = models.UUIDField(
        unique=True,
        default=uuid4,
        editable=False,
        verbose_name=_('UUID')
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    profile_image = models.ImageField(
        verbose_name=_("Profile Image"),
        default="",
        upload_to="",
    )

    about = RichTextField(
        verbose_name=_("About"),
        blank=True,
        null=True,
    )

    activity_start_date = models.DateField(
        verbose_name=_("Activity Start Date"),
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
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        db_table = f"{MODEL_NAME}_articles"



class Blog(models.Model):
    uuid = models.UUIDField(
        unique=True,
        default=uuid4,
        editable=False,
        verbose_name=_('UUID')
    )
    title = models.CharField(
        max_length=100,
        verbose_name=_("Title")
    )

    article = models.ForeignKey(
        Article,
        verbose_name=_("Article")
    )

    tags = models.ManyToManyField(
        Tag,
        verbose_name=_("Tags"),
        blank=True
    )

    study_time = models.CharField(
        max_length=5,
        verbose_name=_("Study Time"),
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
        return self.title

    class Meta:
        """ Description """
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        db_table = f"{MODEL_NAME}"


