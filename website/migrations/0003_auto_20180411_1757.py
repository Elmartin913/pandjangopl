# Generated by Django 2.0.4 on 2018-04-11 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_contact_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='mobile',
            field=models.IntegerField(),
        ),
    ]
