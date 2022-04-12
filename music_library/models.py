from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)

    def __str__(self):
        return self.artist_name

class Album(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    artist = models.ManyToManyField(Artist)
    def __str__(self):
        return self.title

class Song(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.CharField(max_length=200)
    artist = models.ManyToManyField(Artist)
    album = models.ManyToManyField(Album, blank=True)
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

    def __str__(self):
        return self.title
