# Generated by Django 3.2.12 on 2023-08-04 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0019_auto_20230804_0950'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='category',
            index_together=set(),
        ),
        migrations.RemoveField(
            model_name='category',
            name='slug_category',
        ),
    ]
