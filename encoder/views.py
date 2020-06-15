from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
# Create your views here.

def image_upload(request):
    if request.method=='POST':
        form = image_upload_form(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponse("success")

    else:
        form = image_upload_form()
    return render(request, 'upload.html', {'form':form})
    
