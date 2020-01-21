from django.db import models

# Create your models here.


class CalibrationServices(models.Model):

    cali_type = models.CharField(max_length=150, blank=False)
    cali_name = models.CharField(max_length=150, blank=False)
    description = models.TextField()
    start_date = models.DateField(auto_created=True)

    def __str__(self):

        return "c_type:" + self.cali_type + ", c_name:" + self.cali_name + ", c_description:" + self.description
