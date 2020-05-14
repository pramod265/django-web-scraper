from django.contrib.postgres.fields import JSONField
from django.db import models
import jsonfield
# Create your models here.

class SiteData(models.Model):
    data = jsonfield.JSONField(blank=True, default=dict())
    url = models.URLField(blank=True, null=True)
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = "scraper"
        verbose_name = "Site Data"
        verbose_name_plural = "Site Data"

    def __str__(self):
        return str(self.pk)

