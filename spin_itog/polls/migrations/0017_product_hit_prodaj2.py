# Generated by Django 3.2.12 on 2023-08-04 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0016_product_recomend2'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='hit_prodaj2',
            field=models.BooleanField(default=False, verbose_name='Хит продаж2'),
        ),
    ]
