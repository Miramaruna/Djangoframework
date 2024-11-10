# Generated by Django 5.1.3 on 2024-11-10 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155, verbose_name='Заголовка')),
                ('author', models.CharField(max_length=255, verbose_name='Автор')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('pages', models.IntegerField(verbose_name='Количество страниц    ')),
                ('logo', models.ImageField(upload_to='image/')),
            ],
            options={
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.DeleteModel(
            name='News',
        ),
    ]
