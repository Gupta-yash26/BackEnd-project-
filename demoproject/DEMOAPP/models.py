from django.db import models

# Create your models here.
class modelclass(models.Model):
    Name=models.CharField(max_length=100)
    Father_name=models.CharField(max_length=100)
    Mobile_number=models.IntegerField()
    Account_Number=models.BigIntegerField()
    IFSC_code=models.TextField()
    Branch_address=models.TextField()
    passbook_Image=models.ImageField(upload_to = 'SG/')
    
    
