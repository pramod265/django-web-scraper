import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
# Create your views here.
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from scraper.models import SiteData
from scraper.serializers import SiteDataSerializer


class ScrapeSitesViewSet(viewsets.ModelViewSet):
    queryset = SiteData.objects.all()
    serializer_class = SiteDataSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        page = requests.get('https://www.worldometers.info/coronavirus/#countries')
        soup = BeautifulSoup(page.content, 'html.parser')

        # print(soup)
        data = []
        table = soup.find('table', attrs={'class': 'main_table_countries'})
        table_body = table.find('tbody')

        rows = table_body.find_all('tr')

        # total = table_body.find_all('tr', attrs={'class':'total_row'})
        # total = [ele.text.strip() for ele in total]

        th = table.find_all('th')
        th = [ele.text.strip() for ele in th]

        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            data.append([ele for ele in cols])

        return Response(status=status.HTTP_201_CREATED)