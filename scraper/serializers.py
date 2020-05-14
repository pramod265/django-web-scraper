from rest_framework import serializers

from scraper.models import SiteData


class SiteDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = SiteData
        fields = ('id', 'url', 'data', 'category', 'city', 'added_on', 'updated_on')