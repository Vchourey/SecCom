from django.contrib import admin
from Mylearning.models import Interview_QA, Reading_Material, Topic, Reg_Form
# Register your models here.
admin.site.register(Topic)
admin.site.register(Interview_QA)
admin.site.register(Reading_Material)
admin.site.register(Reg_Form)
