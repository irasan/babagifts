# Generated by Django 3.2.6 on 2021-08-28 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0007_alter_subactive_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subactive',
            name='description',
            field=models.CharField(default=' ', max_length=80),
            preserve_default=False,
        ),
    ]