from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import image_upload_form
from .convert import base64_md5
from django.conf import settings
# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from .serializers import image_serializer

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


class image_upload_view(APIView):
    parser_class = (FileUploadParser, )
    def post(self, request):
        file_serializer = image_serializer(data = request.data)
        if file_serializer.is_valid():
            dict = convert_image(request.data['image_main'])
            return JsonResponse(dict ,status=status.HTTP_200_OK)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
