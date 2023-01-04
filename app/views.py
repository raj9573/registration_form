from django.shortcuts import render

# Create your views here.
from app.views import *
from app.forms import * 
from django.http import HttpResponse


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
            return HttpResponse('Your registration is successfully completed ')



    return render(request,'registration.html',d)