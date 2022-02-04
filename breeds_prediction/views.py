import os.path

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.views import APIView

from breeds_prediction.ai_logic.breed_prediction import predict_breed_transfer
from breeds_prediction.tasks import predict_breed_transfer_task
from neural_models_api.custom_storages import default_file_storage


class BreedPredictionAPI(APIView):
    def post(self, request):
        print('predicting the dog breed', flush=True)
        image = request.FILES.get('image_to_predict')
        url = default_file_storage.save(os.path.join('tmp/', image.name), image)
        breed = predict_breed_transfer_task.delay(url)
        return JsonResponse(data={'breed': breed.get()}, status=200)
