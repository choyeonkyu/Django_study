# Generated by Django 5.1.1 on 2024-10-08 07:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("polls", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="pub_date",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
