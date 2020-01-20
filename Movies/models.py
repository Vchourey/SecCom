from django.db import models


class Movies(models.Model):
    movie_title = models.CharField(max_length=200)
    movie_category = models.CharField(max_length=200)
    duration = models.IntegerField()
    release_year = models.CharField(max_length=300)
    actor = models.CharField(max_length=200)
    director = models.CharField(max_length=200)

    def __str__(self):
        return "Movie name:" + self.movie_title +", category"+ self.movie_category+ ", directed by:" + self.director
