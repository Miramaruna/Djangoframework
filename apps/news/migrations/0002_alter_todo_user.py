# Generated by Django 5.1.2 on 2024-11-26 01:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='user',
            field=models.ManyToManyField(blank=True, related_name='ggg', to=settings.AUTH_USER_MODEL),
        ),
    ]