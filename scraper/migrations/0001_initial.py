# Generated by Django 3.0.6 on 2020-05-14 06:20

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', jsonfield.fields.JSONField(blank=True, default={})),
                ('url', models.URLField(blank=True, null=True)),
                ('category', models.CharField(max_length=50, blank=True, null=True)),
                ('city', models.CharField(max_length=50, blank=True, null=True)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Site Data',
                'verbose_name_plural': 'Site Data',
            },
        ),
    ]
