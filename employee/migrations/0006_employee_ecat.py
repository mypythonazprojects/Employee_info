# Generated by Django 2.2 on 2019-04-21 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_auto_20190422_0026'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='ecat',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]