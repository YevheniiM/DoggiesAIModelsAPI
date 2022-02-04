from breeds_prediction.ai_logic.breed_prediction import predict_breed_transfer
from neural_models_api.celery import app
from neural_models_api.custom_storages import default_file_storage


@app.task
def predict_breed_transfer_task(image_path):
    print(f'started dog prediction: {image_path}')
    return predict_breed_transfer(img_path=image_path)
