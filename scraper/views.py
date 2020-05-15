import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
# Create your views here.
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from scraper.mixin import get_websites_data, scrape_url
from scraper.models import SiteData
from scraper.serializers import SiteDataSerializer


class ScrapeSitesViewSet(viewsets.ModelViewSet):
    queryset = SiteData.objects.all()
    serializer_class = SiteDataSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        data = request.data

        threshold = data.get('threshold', 10) # default 10
        url = data.get('url', None)

        if url:
            data = scrape_url(url)
            SiteData.objects.create(
                url=url,
                data=data
            )

        else:
            page, temp = 1, 0
            while True:

                if threshold >= 20:
                    threshold -= 20
                    temp = 20
                elif 0 < threshold < 20:
                    temp = threshold
                    threshold = 0
                else:
                    break

                data = get_websites_data(threshold=temp, page=page)
                model_objects = [SiteData(url=i["url"],category=i["category"],city=i["city"],data=i["data"]) for i in data]
                SiteData.objects.bulk_create(model_objects)

                page += 1
                # temp = threshold


        return Response(data, status=status.HTTP_201_CREATED)