# Generated by Django 3.1.5 on 2021-01-14 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_profile_info"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="info",
            field=models.TextField(blank=True, max_length=350, null=True),
        ),
    ]