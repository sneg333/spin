# Generated by Django 3.2.12 on 2023-08-03 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_carusel'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='carusel_home_page2',
            field=models.BooleanField(default=False, verbose_name='баннер главная страница справа'),
        ),
        migrations.AlterField(
            model_name='product',
            name='carusel_home_page',
            field=models.BooleanField(default=False, verbose_name='баннер главная страница слева'),
        ),
    ]
