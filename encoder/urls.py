from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import image_upload, image_upload_view

urlpatterns=[
    path('', image_upload, name="uploader"),
    path('apiendpoint/', image_upload_view.as_view(), name="api_endpoint")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
