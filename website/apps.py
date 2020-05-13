from django.apps import AppConfig
from django.conf import settings
import os,pickle
from tensorflow.keras.models import load_model


class WebsiteConfig(AppConfig):
    name = 'website'

    path = os.path.join(settings.MODEL_PATH, 'models.p')
    local_model = os.path.join(settings.MODEL_PATH, 'cbds.h5')

    with open(path, 'rb') as pickled:
        data = pickle.load(pickled)

    model = load_model(local_model)
    tokenizer = data['tokenizer']