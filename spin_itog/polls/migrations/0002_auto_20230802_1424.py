# Generated by Django 3.2.12 on 2023-08-02 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='hit_prodaj',
            field=models.BooleanField(default=False, verbose_name='Хит продаж'),
        ),
        migrations.AddField(
            model_name='product',
            name='recomend',
            field=models.BooleanField(default=False, verbose_name='Рекомендуемые'),
        ),
    ]
