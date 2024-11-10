from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    author = models.CharField(
        max_length=255,
        verbose_name='Автор'
    )
    date = models.DateField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    pages = models.IntegerField(
        verbose_name='Количество страниц    '
    )
    logo = models.ImageField(
        upload_to='image/',
        null=True
    )
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Новости'