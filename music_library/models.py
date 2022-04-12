from django.db import models

class Artist(models.Model):
    artist_name = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)

class Albums(models.Model):
    title = models.CharField(blank=False, null=False, max_length=200)
    release_date = models.CharField(blank=False, null=False, max_length=200)
    publisher = models.CharField(blank=False, null=False, max_length=200)

class Songs(models.Model):
    title = models.CharField(blank=False, null=False, max_length=200)
    release_date = models.CharField(blank=False, null=False, max_length=200)
    YES = 'Y'
    NO = 'N'
    EXPLICIT_CONTENT_CHOICES = [
        (YES, 'Yes'),
        (NO, 'No'),
    ]
    explicit_content = models.CharField(
        max_length = 1,
        choices = EXPLICIT_CONTENT_CHOICES,
        default = YES,
    )
