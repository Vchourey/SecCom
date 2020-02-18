from django.db import models


class ContactDetail(models.Model):

    branch_name = models.CharField(max_length=150)
    address_line = models.TextField()
    email = models.EmailField()
    phone = models.IntegerField()
    mobile = models.IntegerField()
    contact_Person = models.CharField(max_length=100)

    def __str__(self):

        return str(self.branch_name)


class Enquiry(models.Model):
    enq_num = models.AutoField(primary_key=True, auto_created=True)
    company_enquire_name = models.CharField(max_length=200, blank=False)
    email = models.EmailField(blank=True)
    phone = models.IntegerField(blank=False, )
    address_location = models.CharField(max_length=200, blank=False)
    service_product = models.CharField(max_length=200)
    requirements = models.TextField(blank=True)
    file = models.FileField(upload_to="enquiry/files/", blank=True, null=True)
    enquiry_date = models.DateTimeField(auto_now=True)

    def __str__(self):

        return str(self.enq_num) + ", "+str(self.company_enquire_name) + ", " + str(self.phone) + ", " + str(self.enquiry_date)
