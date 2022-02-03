from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.views import APIView

from breeds_prediction.ai_logic.breed_prediction import predict_breed_transfer


class BreedPredictionAPI(APIView):
    def post(self, request):
        print('predicting the dog breed', flush=True)
        image = request.FILES.get('image_to_predict')
        breed = predict_breed_transfer(image=image.read())
        return JsonResponse(data={'breed': breed}, status=200)
