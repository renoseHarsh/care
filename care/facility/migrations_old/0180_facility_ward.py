# Generated by Django 2.2.11 on 2020-09-21 12:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0030_auto_20200921_1659"),
        ("facility", "0179_auto_20200918_1132"),
    ]

    operations = [
        migrations.AddField(
            model_name="facility",
            name="ward",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="users.Ward",
            ),
        ),
    ]