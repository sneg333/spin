# Generated by Django 3.2.12 on 2023-08-04 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0018_product_new_tovar2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='podcategory',
        ),
        migrations.AddField(
            model_name='category',
            name='product',
            field=models.ManyToManyField(to='polls.Product', verbose_name='товар'),
        ),
        migrations.DeleteModel(
            name='PodCategory',
        ),
    ]
