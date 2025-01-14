# Generated by Django 5.1.1 on 2024-10-10 02:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("polls", "0002_alter_question_pub_date"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="question",
            name="owner",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="questions",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="question",
            name="pub_date",
            field=models.DateTimeField(auto_now_add=True, verbose_name="생성일"),
        ),
        migrations.AlterField(
            model_name="question",
            name="question_text",
            field=models.CharField(max_length=200, verbose_name="질문"),
        ),
    ]
