# Generated by Django 2.2.2 on 2019-06-29 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0007_auto_20190629_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='presentation',
            name='event_id',
            field=models.CharField(blank=True, max_length=39),
        ),
    ]
