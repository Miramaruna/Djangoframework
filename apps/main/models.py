from django.db import models

# Create your models here.
class Settings(models.Model):
    created = models.DateField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    title = models.CharField(
        max_length=155,
        verbose_name="Заголовок"
        
    )
    description = models.TextField(
        verbose_name="Описание"
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = ""
        verbose_name_plural = "Основные настройки"
    