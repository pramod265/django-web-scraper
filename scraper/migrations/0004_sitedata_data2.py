# Generated by Django 3.0.6 on 2020-05-15 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0003_auto_20200515_0942'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitedata',
            name='data2',
            field=models.TextField(blank=True, null=True),
        ),
    ]
