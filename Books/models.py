from django.db import models


class Books(models.Model):
    book_id = models.IntegerField()
    book_title = models.CharField(max_length=200)
    book_subject = models.CharField(max_length=200)
    book_publisher = models.CharField(max_length=200)
    book_author = models.CharField(max_length=300)

    def __str__(self):
        return str(self.book_id) + "," + self.book_title + "," + self.book_subject


class Donner(models.Model):
    Books = models.ForeignKey(Books, on_delete=models.CASCADE)
    member_id = models.IntegerField()
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)

    def __str__(self):

        return str(self.member_id) + "," + self.first_name + "," + self.last_name
