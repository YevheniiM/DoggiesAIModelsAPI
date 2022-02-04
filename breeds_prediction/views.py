import os.path

from django.core.files.storage import default_storage
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.views import APIView

from breeds_prediction.ai_logic.breed_prediction import predict_breed_transfer
from breeds_prediction.tasks import predict_breed_transfer_task


class BreedPredictionAPI(APIView):
    def post(self, request):
        print('predicting the dog breed', flush=True)
        try:
            image = request.FILES.get('image_to_predict')
            path = default_storage.save(os.path.join('tmp/', image.name), image)
            breed = predict_breed_transfer_task.delay(path)
            return JsonResponse(data={'breed': breed.get()}, status=200)
        except Exception as ex:
            print("Error:", ex)
            return HttpResponse(status=400)
