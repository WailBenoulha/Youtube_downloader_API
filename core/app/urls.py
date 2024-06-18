from django.contrib import admin
from django.urls import path
from .views import DownloaderView

urlpatterns = [
    path('youtube/', DownloaderView.as_view())
]
