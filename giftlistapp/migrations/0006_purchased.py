# Generated by Django 2.1.5 on 2019-12-19 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('giftlistapp', '0005_auto_20191219_1907'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchased',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='giftlistapp.Product')),
            ],
        ),
    ]
