# Generated by Django 3.0.7 on 2020-07-27 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0018_auto_20200727_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinformation',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
