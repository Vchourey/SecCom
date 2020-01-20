from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=True)

    # Additional
    profile_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return str(self.user.username)


class CompanyServices(models.Model):
    service_id = models.IntegerField()
    service_name = models.CharField()
    description = models.TextField()
    service_had = models.CharField
    contact = models.IntegerField()
    start_date = models.DateField()


class CalibrationServices(models.Model):

    type = models.CharField(max_length=150, blank=False)
    name = models.CharField(max_length=150, blank= False)
    description = models.TextField()
    start_date = models.DateField()

