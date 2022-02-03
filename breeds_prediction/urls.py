from django.contrib import admin
from django.urls import path, include

from breeds_prediction.views import predict_breed

urlpatterns = [
    path('predict/', predict_breed),
]