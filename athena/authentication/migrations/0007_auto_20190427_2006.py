# Generated by Django 2.2 on 2019-04-27 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_auto_20190427_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='cipher',
            field=models.CharField(max_length=15, null=True, unique=True),
        ),
    ]
