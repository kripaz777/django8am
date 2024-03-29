# Generated by Django 4.1.4 on 2022-12-28 03:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=300)),
                ("price", models.IntegerField()),
                ("discounted_price", models.IntegerField(default=0)),
                ("image", models.ImageField(upload_to="media")),
                ("description", models.TextField()),
                ("specification", models.TextField()),
                ("slug", models.TextField()),
                (
                    "stock",
                    models.CharField(
                        choices=[
                            ("In stock", "In stock"),
                            ("Out of stock", "Out of stock"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "label",
                    models.CharField(
                        choices=[
                            ("new", "new"),
                            ("hot", "hot"),
                            ("sale", "sale"),
                            ("", "default"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "brand",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="home.brand"
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="home.category"
                    ),
                ),
                (
                    "subcategory",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="home.subcategory",
                    ),
                ),
            ],
        ),
    ]
