# Generated by Django 5.1.2 on 2024-11-02 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Названия сайта')),
                ('description', models.TextField(verbose_name='Описания сайта')),
                ('logo', models.ImageField(upload_to='logo/', verbose_name='Логотип сайта')),
            ],
            options={
                'verbose_name': 'Основная настройка',
                'verbose_name_plural': 'Основные настройки',
            },
        ),
    ]