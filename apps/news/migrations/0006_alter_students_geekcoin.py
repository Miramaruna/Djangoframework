# Generated by Django 5.1.2 on 2024-11-22 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_alter_students_geekcoin_alter_transaction_fromuser_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='geekcoin',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]