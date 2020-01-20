from django.db import models
from django import forms


class Topic(models.Model):
    subject = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.subject


class Interview_QA(models.Model):

    subject = models.ForeignKey(Topic, on_delete=models.CASCADE)
    question_num = models.IntegerField()
    question_des = models.CharField(max_length=100)
    answer = models.CharField(max_length=2000)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return str(self.question_num) + ", " + self.question_des


    class Meta:

        db_table = 'Interview_QA'


class Reading_Material(models.Model):

    subject = models.ForeignKey(Topic, on_delete=models.CASCADE)
    document = models.FileField(upload_to='document/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return str(self.document)

    class Meta:
        db_table = 'reading_material'


class Reg_Form(models.Model):

    FiestName = models.CharField(max_length=50)
    LasteName = models.CharField(max_length=50)
    EmailStu = models.EmailField(default='vijay@gmail.com')
    TextArea = models.TextField(default='no comments')

    def __str__(self):

        return str(self.FiestName) + ", " + self.LasteName

