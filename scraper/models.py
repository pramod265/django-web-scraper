from django.contrib.postgres.fields import JSONField
from django.db import models
import jsonfield
# Create your models here.

class SiteData(models.Model):
    url = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    data = jsonfield.JSONField(blank=True, default=dict())
    # data2 = models.TextField(blank=True, null=True) # TextField Do not process \n
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = "scraper"
        verbose_name = "Site Data"
        verbose_name_plural = "Site Data"

    def __str__(self):
        return str(self.pk)

