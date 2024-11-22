from django.db import models

# Create your models here.

class Authors(models.Model):
    # category = models.OneToOneField(Books, on_delete=models.CASCADE, null=True, blank=True)

    name = models.CharField(
        max_length=255,
        verbose_name='Имя автора',
        unique=True
    )
    birthdate = models.DateField(
        verbose_name='День рождения автора'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Авторы'

class Books(models.Model):
    title = models.TextField(
        verbose_name='Название книги'
    )
    publication_year = models.DateField(
        verbose_name='Год издания'
    )
    authors = models.ForeignKey(Authors, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Книги"

class Genre(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Название жанра'
    )
    books = models.ManyToManyField(Books,)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Жанры"