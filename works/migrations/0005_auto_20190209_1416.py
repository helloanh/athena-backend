# Generated by Django 2.1.5 on 2019-02-09 11:16

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("edu", "0006_auto_20190209_1416"),
        ("authentication", "0003_auto_20190209_1340"),
        ("works", "0004_auto_20190209_1304"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="report", unique_together={("task", "student")}
        ),
        migrations.AlterUniqueTogether(
            name="task", unique_together={("subject", "theme")}
        ),
    ]
