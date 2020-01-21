from django.contrib import admin
from .models import UserProfileInfo, CompanyServices, ContactDetail

# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(CompanyServices)
admin.site.register(ContactDetail)
