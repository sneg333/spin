# Generated by Django 3.2.12 on 2023-08-04 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0015_product_samie_prodavaemie'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='recomend2',
            field=models.BooleanField(default=False, verbose_name='Рекомендуемые2'),
        ),
    ]
