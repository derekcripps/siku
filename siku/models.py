from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=200)


class Album(models.Model):
    name = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE())
    release_date = models.DateField()
    rating = models.IntegerField()
    image = models.ImageField(upload_to='albums')

    def __str__(self):
        return self. name


class Track(models.Model):
    track = models.IntegerField()
    name = models.CharField(max_length=200)
    album = models.ManyToManyField(Album)
    track_location = models.FileField(upload_to='music')

    def __str__(self):
        return self.name


class Playlist(models.Model):
    name = models.CharField(max_length=200)
    track = models.ForeignKey(Track)

    def __str__(self):
        return self.name



