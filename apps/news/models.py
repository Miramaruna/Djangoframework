from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Название рецепта'
    )
    ingredients = models.TextField(
        verbose_name='Ингредиенты'
    )
    instruction = models.TextField(
        verbose_name='Инструкция для приготовления'
    )
    prep_time = models.IntegerField(
        verbose_name='Время приготовления в минутах'
    )
    is_vegetarian = models.BooleanField(
        verbose_name='Вегатарианское блюдо?'
    )
    created_at = models.DateField(
        verbose_name='Дата добавления предмета',
        auto_now_add=True
    )
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Рецепты'