from django.contrib import admin
from .models import *
# Register your models here.
class adminmodel(admin.ModelAdmin):
    list_display=['Name','Father_name','Mobile_number','Account_Number','IFSC_code','Branch_address','passbook_Image']
admin.site.register(modelclass,adminmodel)