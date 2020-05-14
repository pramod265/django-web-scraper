from django.contrib import admin

# Register your models here.
from scraper.models import SiteData


class SiteDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'url', 'data', 'added_on', 'updated_on')
    list_filter = ('added_on', 'updated_on')
    search_fields = ('url', 'data')


admin.site.register(SiteData, SiteDataAdmin)