# Generated by Django 2.2.2 on 2019-06-30 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0012_auto_20190630_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='attend_presentations',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='conference.Presentation'),
        ),
    ]
