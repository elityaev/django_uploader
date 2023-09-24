from django.urls import path

from .views import FileUploadAPIView, FileList

app_name = 'api'

urlpatterns = [
    path('upload/', FileUploadAPIView.as_view(), name='upload'),
    path('files/', FileList.as_view(), name='files')
]