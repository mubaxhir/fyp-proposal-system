# Generated by Django 4.2.1 on 2023-05-19 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_proposalreview_datetime"),
    ]

    operations = [
        migrations.AddField(
            model_name="proposal",
            name="datetime",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
