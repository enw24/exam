# Generated by Django 3.0 on 2019-12-15 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('giftlistapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='url',
            field=models.URLField(default='espn.com', max_length=2000),
        ),
    ]
