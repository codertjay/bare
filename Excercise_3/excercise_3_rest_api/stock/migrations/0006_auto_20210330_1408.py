# Generated by Django 3.1.7 on 2021-03-30 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0005_auto_20210330_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='price',
            field=models.FloatField(),
        ),
    ]
