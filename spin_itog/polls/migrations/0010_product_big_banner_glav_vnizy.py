# Generated by Django 3.2.12 on 2023-08-03 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_auto_20230803_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='big_banner_glav_vnizy',
            field=models.BooleanField(default=False, verbose_name='большой баннер на главной странице внизу'),
        ),
    ]