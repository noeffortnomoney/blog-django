# Generated by Django 4.1.2 on 2022-10-13 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="postmodel", options={"ordering": ("-date_created",)},
        ),
    ]
