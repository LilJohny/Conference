# Generated by Django 2.2.2 on 2019-06-30 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0014_auto_20190630_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='gallery'),
        ),
    ]
