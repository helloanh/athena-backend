# Generated by Django 2.2 on 2019-04-27 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_auto_20190417_0705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='cipher',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True),
        ),
    ]
