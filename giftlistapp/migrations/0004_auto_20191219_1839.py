# Generated by Django 2.1.5 on 2019-12-19 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('giftlistapp', '0003_auto_20191215_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='css/None/no-img.jpg', upload_to='css/'),
        ),
    ]
