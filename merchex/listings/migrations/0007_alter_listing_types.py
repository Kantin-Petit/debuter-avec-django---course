# Generated by Django 5.0 on 2023-12-26 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0006_listing_band'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='types',
            field=models.CharField(choices=[('Records', 'Records'), ('Clothing', 'Clothing'), ('Posters', 'Posters'), ('Misc', 'Miscellaneous')], max_length=15),
        ),
    ]
