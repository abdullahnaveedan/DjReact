# Generated by Django 4.2.10 on 2024-02-12 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("stname", models.CharField(max_length=50)),
                ("stemail", models.EmailField(max_length=254)),
            ],
        ),
    ]
