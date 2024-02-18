# Generated by Django 5.0.1 on 2024-02-17 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Forum",
            fields=[
                ("thread_id", models.AutoField(primary_key=True, serialize=False)),
                ("creator", models.CharField(max_length=255)),
                ("content", models.TextField()),
                ("category", models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="News",
            fields=[
                ("news_id", models.AutoField(primary_key=True, serialize=False)),
                ("date", models.DateField()),
                ("content_text", models.TextField()),
                ("content_img", models.TextField()),
                ("category", models.CharField(blank=True, max_length=255, null=True)),
                ("likes", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="News_comments",
            fields=[
                ("comment_id", models.AutoField(primary_key=True, serialize=False)),
                ("author_name", models.TextField()),
                ("authot_img", models.TextField()),
                ("date", models.DateField()),
                ("content", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="User",
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
                ("email", models.EmailField(max_length=254, unique=True)),
                ("username", models.CharField(max_length=30, unique=True)),
                ("password", models.CharField(max_length=128)),
                ("info", models.TextField(blank=True)),
                (
                    "role",
                    models.CharField(
                        choices=[("user", "User"), ("admin", "Admin")],
                        default="user",
                        max_length=20,
                    ),
                ),
                ("active", models.BooleanField(default=True)),
                ("profile_img", models.TextField()),
            ],
        ),
    ]