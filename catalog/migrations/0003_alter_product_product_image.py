# Generated by Django 5.1.4 on 2025-01-29 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0002_contact"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="product_image",
            field=models.ImageField(
                blank=True, null=True, upload_to="images/", verbose_name="Saved image"
            ),
        ),
    ]
