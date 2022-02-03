from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_http_methods

from breeds_prediction.ai_logic.breed_prediction import predict_breed_transfer


@ensure_csrf_cookie
@require_http_methods(["POST"])
def predict_breed(request):
    image = request.FILES.get('image_to_predict')
    breed = predict_breed_transfer(image=image.read())
    return JsonResponse(data={'breed': breed}, status=200)
