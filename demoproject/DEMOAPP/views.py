from django.shortcuts import render,redirect
from .models import*

# Create your views here.
def acco_view(request):
    if request.method=='POST':
        print(123)
        data=request.POST
        name=data.get('holder')
        name1=data.get('fathername')
        name2=data.get('number')
        name3=data.get('account')
        name4=data.get('code')
        name5=data.get('address')
        name6=request.FILES.get('image')
        print(name,name1,name2,name3,name4,name5,name6)
        ab=modelclass(Name=name,Father_name=name1,Mobile_number=name2,Account_Number=name3,IFSC_code=name4,Branch_address=name5,passbook_Image=name6)
        ab.save()
        
    return render(request, 'yash.html')
            
        
        