# Generated by Django 3.2.6 on 2021-08-28 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0004_auto_20210828_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subactive',
            name='end_date',
            field=models.DateTimeField(default='timezone.now'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='duration',
            field=models.IntegerField(default=1),
        ),
    ]
