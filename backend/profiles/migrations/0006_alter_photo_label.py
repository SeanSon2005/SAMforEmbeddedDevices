# Generated by Django 5.0.6 on 2024-05-31 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0005_alter_photo_dataset"),
    ]

    operations = [
        migrations.AlterField(
            model_name="photo",
            name="label",
            field=models.CharField(blank=True, default="", max_length=255),
        ),
    ]
