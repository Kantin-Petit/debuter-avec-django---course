# Generated by Django 5.0 on 2023-12-26 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0008_alter_listing_types'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='like_new',
            field=models.BooleanField(default=False),
        ),
    ]
