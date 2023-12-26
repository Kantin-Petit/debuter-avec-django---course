# Generated by Django 5.0 on 2023-12-26 06:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_band_activre_band_biography_band_genre_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='description',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='sold',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='listing',
            name='types',
            field=models.CharField(choices=[('Records', 'Records'), ('Clothing', 'Clothing'), ('Posters', 'Posters'), ('Miscellaneous', 'Miscellaneous')], default='Records', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='year',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2023)]),
        ),
    ]
