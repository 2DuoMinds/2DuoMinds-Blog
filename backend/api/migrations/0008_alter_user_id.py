# Generated by Django 5.0.1 on 2024-02-18 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0007_remove_user_token"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="id",
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]
