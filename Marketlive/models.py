from django.db import models

# Create your models here.

class share_list(models.Model):

    companey_name = models.CharField(max_length=50)
    parent_companey = models.CharField(max_length=50)
    share_current_Price = models.IntegerField()
    share_open_Price = models.IntegerField()
    share_close_Price = models.IntegerField()
    trade_volume = models.CharField(max_length=2000)
    listing_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'share_list'
