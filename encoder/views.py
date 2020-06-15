from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import image_upload_form
from .convert import base64_md5
from django.conf import settings
# Create your views here.

def image_upload(request):
    if request.method=='POST':
        form = image_upload_form(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            image = request.FILES['image_main']
            my_encode = convert_image(image)
            return JsonResponse(my_encode)
            #return render(request, 'result.html', my_encode)

    else:
        form = image_upload_form()
    return render(request, 'upload.html', {'form':form})

def convert_image(image):
    '''
    This function takes the name of image from form and joins it with the
    path of the media\images folder with image. The raw string of the image
    address is read as binary ('rb') and is passed to base64_md5 function.
    '''
    image_location = settings.BASE_DIR + '\media\images\{}'.format(image)
    #with open(image_location, 'rb') as img:
    img = open(r'''{}'''.format(image_location), 'rb')
    encryts = base64_md5(img)
    return encryts
