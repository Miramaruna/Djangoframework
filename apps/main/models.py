from django.db import models

# Create your models here.

class Settings(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Названия сайта"
    )
    description = models.TextField(
        verbose_name='Описания сайта'
    )
    logo = models.ImageField(
        verbose_name='Логотип сайта',
        upload_to="logo/"
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Основная настройка"
        verbose_name_plural = "Основные настройки"