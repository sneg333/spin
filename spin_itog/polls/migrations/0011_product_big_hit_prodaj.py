# Generated by Django 3.2.12 on 2023-08-03 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_product_big_banner_glav_vnizy'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='big_hit_prodaj',
            field=models.BooleanField(default=False, verbose_name='Большая фото Хит продаж'),
        ),
    ]
