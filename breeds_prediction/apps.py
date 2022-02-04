import io
import os.path

import torch
import torch.nn as nn
import torchvision.models as models
from django.apps import AppConfig
from django.conf import settings
from django.core.files.storage import default_storage
from torch import optim

from neural_models_api.custom_storages import default_file_storage


class BreedPredictionModel:
    def __init__(self):
        self.model = models.vgg16()

        if settings.DEBUG:
            with open(os.path.join(settings.MODELS_PATH, 'breeds.txt'), 'r') as f:
                self.class_names = [n.strip() for n in f.readlines()]
        else:
            with default_file_storage.open(os.path.join(settings.MODELS_PATH, 'breeds.txt'), "r") as f:
                self.class_names = [n.decode("utf-8").strip() for n in f.readlines()]

        for param in self.model.features.parameters():
            param.requires_grad = False

        n_inputs = self.model.classifier[6].in_features

        last_layer = nn.Linear(n_inputs, 133)

        self.model.classifier[6] = last_layer
        # criterion_transfer = nn.CrossEntropyLoss()
        # optimizer_transfer = optim.SGD(self.model.classifier.parameters(), lr=0.001)

        if settings.DEBUG:
            print(f"DEBUG: Initializing model [{os.path.join(settings.MODELS_PATH, 'breed_prediction.pt')}]")
            with default_storage.open(os.path.join(settings.MODELS_PATH, 'breed_prediction.pt'), "rb") as f:
                self.model.load_state_dict(torch.load(io.BytesIO(f.read())))
        else:
            print(f"INFO: Initializing model [{os.path.join(settings.MODELS_PATH, 'breed_prediction.pt')}]")
            with default_file_storage.open(os.path.join(settings.MODELS_PATH, 'breed_prediction.pt'), "rb") as f:
                self.model.load_state_dict(torch.load(io.BytesIO(f.read())))


class BreedsPredictionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'breeds_prediction'
    init_model = BreedPredictionModel()
    model = init_model.model
    class_names = init_model.class_names

    # if os.environ.get('RUN_MAIN', None) != 'true':

