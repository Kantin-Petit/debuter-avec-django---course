from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Band(models.Model):

    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'

    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(
        choices=Genre.choices,
        max_length=5
    )
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2023)]
    )
    activre = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)

class Listing(models.Model):

    class Type(models.TextChoices):
        RECORDS = 'Records'
        CLOTHING = 'Clothing'
        POSTERS = 'Posters'
        MISCELLANEOUS = 'Miscellaneous'

    title = models.CharField(max_length=100)
    types = models.CharField(
        choices=Type.choices,
        max_length=15
    )
    description = models.CharField(max_length=1000)
    year = models.IntegerField(
        null=True, 
        validators=[MinValueValidator(1900), MaxValueValidator(2023)]
    )
    sold = models.BooleanField(default=False)