# Generated by Django 4.2.3 on 2023-08-01 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finalapplication', '0005_product_date_of_arrival_sale_date_of_arrival'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sale',
            old_name='date_of_arrival',
            new_name='date_of_sale',
        ),
    ]