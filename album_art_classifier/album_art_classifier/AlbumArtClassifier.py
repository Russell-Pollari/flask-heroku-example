import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array

from album_art_classifier.model import model as _model


class AlbumArtClassifier:
	def __init__(self):
		self.model = _model

	def load_weights(self, file):
		self.model = load_model(file)

	def classify_one(self, file):
		x = img_to_array(load_img(file)) / 255

		pred = self.model.predict(np.expand_dims(x, axis=0))

		genre = 'metal' if pred[0][0] < 0.5 else 'not_metal'

		return genre, pred[0][0]
