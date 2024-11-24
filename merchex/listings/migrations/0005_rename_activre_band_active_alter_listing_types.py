# Generated by Django 5.0 on 2023-12-26 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_listing_description_listing_sold_listing_types_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='band',
            old_name='activre',
            new_name='active',
        ),
        migrations.AlterField(
            model_name='listing',
            name='types',
            field=models.CharField(choices=[('Records', 'Records'), ('Clothing', 'Clothing'), ('Posters', 'Posters'), ('Miscellaneous', 'Miscellaneous')], max_length=15),
        ),
    ]
