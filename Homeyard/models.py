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

    service_id = models.IntegerField(unique=True)
    service_name = models.CharField(max_length=150)
    description = models.TextField()
    service_had = models.CharField(max_length=150)
    contact_had = models.IntegerField()
    start_date = models.DateField(auto_now_add=True)
