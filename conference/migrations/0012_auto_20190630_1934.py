# Generated by Django 2.2.2 on 2019-06-30 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0011_auto_20190630_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
