# Generated by Django 2.0 on 2018-05-20 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0016_auto_20180520_2017'),
    ]

    operations = [
        migrations.AddField(
            model_name='repository',
            name='parent',
            field=models.CharField(default='', max_length=200),
        ),
    ]