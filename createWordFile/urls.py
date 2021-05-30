from django.urls import path
from .views import Index, CreateFile, EditFile, ViewFile, DeleteFile, Download

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('create', CreateFile.as_view(), name='create'),
    path('edit/<str:pk>', EditFile.as_view(), name='editFile'),
    path('details/<str:pk>', ViewFile.as_view(), name='viewFile'),
    path('delete/<str:pk>', DeleteFile.as_view(), name='deleteFile'),
    path('download/<str:pk>', Download.as_view(), name='download')
]