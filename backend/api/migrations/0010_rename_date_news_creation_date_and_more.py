# Generated by Django 5.0.2 on 2024-02-19 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0009_alter_forum_thread_id_alter_news_news_id_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="id",
            new_name="user_id",
        ),
        migrations.AlterField(
            model_name="forum",
            name="thread_id",
            field=models.AutoField(primary_key=True, serialize=False),
        )
    ]