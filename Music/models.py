from django.db import models


class Album(models.Model):
    artist = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    logo = models.CharField(max_length=300)


    def __str__(self):
        return "Album title:" + self.title +", Artiest:"+ self.artist +", Gener:"+ self.genre +", Logo:"+ self.logo


class Song(models.Model):
    Album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)

    def __str__(self):
        return  "Song title:" + self.song_title +"."+ self.file_type
