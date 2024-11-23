from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.

class Students(AbstractUser):
    # category = models.OneToOneField(Category, on_delete=models.SET_NULL, null=True, blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='students_groups',
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
        related_query_name='student'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='students_permissions',
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
        related_query_name='student'
    )

    username = models.CharField(
        max_length=255,
        verbose_name='Имя ученика',
        unique=True
    )
    geekcoin = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = 'Ученики'

class Transaction(models.Model):
    fromuser = models.ForeignKey(Students, on_delete=models.CASCADE, related_name='хз')

    touser = models.ForeignKey(Students, on_delete=models.CASCADE)

    amount = models.IntegerField(
        verbose_name='Количество передаваемых коинов'
    )
    created_at = models.DateField(
        verbose_name='Дата создания транзакции',
        auto_now_add=True
    )

    def __str__(self):
        return f"Транзакции"
    
    class Meta:
        verbose_name_plural = "Транзакции"