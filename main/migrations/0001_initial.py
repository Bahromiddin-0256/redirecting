# Generated by Django 4.1.3 on 2022-11-25 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Settings",
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
                ("use_example_link", models.BooleanField(default=False)),
                (
                    "example_link",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
            ],
        ),
    ]
