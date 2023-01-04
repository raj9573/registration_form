from django.shortcuts import render

# Create your views here.
from app.views import *
from app.forms import * 
from django.core.mail import send_mail
from django.http import HttpResponse
 

def home(request):
    return render(request,'home.html')
def dummy(request):
    return render(request,'dummy.html')

def  registration(request):
    fd=UserForm()
    pd=Profile()
    d={'fd':fd,'pd':pd}
    if request.method=='POST' and request.FILES:

        ud=UserForm(request.POST)
        pod=Profile(request.POST,request.FILES)
        
        if ud.is_valid() and pod.is_valid():
            USO=ud.save(commit=False)
            pw=ud.cleaned_data['password']
            USO.set_password(pw)
            USO.save()

            PO=pod.save(commit=False)
            PO.user=USO
            PO.save()


            send_mail('User Registration',
                    'Registration is succsfull',
                    'kalamallarajasekhar@gmail.com',
                    [USO.email],fail_silently=False)
                    
            return HttpResponse('Your registration is successfully completed ')



    return render(request,'registration.html',d)