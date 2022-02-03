from django.contrib import admin
from django.urls import path, include

from breeds_prediction.views import BreedPredictionAPI

urlpatterns = [
    path('predict/', BreedPredictionAPI.as_view()),
]