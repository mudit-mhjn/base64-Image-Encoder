from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import image_upload_form
from .convert import base64_md5
# Create your views here.

def image_upload(request):
    if request.method=='POST':
        form = image_upload_form(request.POST, request.FILES)

        if form.is_valid():
            #print(form)
            form.save()
            my_encode = convert_image(form)
            return JsonResponse(my_encode)
            #return render(request, 'result.html', my_encode)

    else:
        form = image_upload_form()
    return render(request, 'upload.html', {'form':form})

def convert_image(form):
    image_tag = form.cleaned_data['image_tag']
    image = form.cleaned_data['image_main']
    d = base64_md5(image) #This is causing error because not passing image as binary.
    # # TODO: convert image to binary
    return d
