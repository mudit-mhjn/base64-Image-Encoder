from django import forms
from .models import *

class image_upload_form(forms.ModelForm):

    class Meta:
        model = images
        fields = ['image_main']
