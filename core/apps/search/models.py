from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.




MODEL_NAME = "search"



class Tag(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name=_("Tag Name")
    )
    slug = models.SlugField(
        max_length=100,
        verbose_name=_("Tag Slug")
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
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        db_table = f"{MODEL_NAME}_tags"
