# Generated by Django 2.0.4 on 2018-04-18 16:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20180418_1458'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='time_add',
        ),
        migrations.AddField(
            model_name='contact',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
