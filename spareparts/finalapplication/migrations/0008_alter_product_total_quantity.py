# Generated by Django 4.2.3 on 2023-08-08 07:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalapplication', '0007_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='total_quantity',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
