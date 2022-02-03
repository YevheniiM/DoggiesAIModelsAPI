from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie

from breeds_prediction.ai_logic.breed_prediction import predict_breed_transfer


@ensure_csrf_cookie
def predict_breed(request):
    if request.method == 'POST':
        print('predicting the dog breed', flush=True)
        image = request.FILES.get('image_to_predict')
        breed = predict_breed_transfer(image=image.read())
        return JsonResponse(data={'breed': breed}, status=200)
    else:
        print('not a POST request', flush=True)
        return HttpResponse(status=200)
