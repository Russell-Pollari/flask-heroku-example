import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array


def predict(model, file):
	# TODO: check file type and format etc
	x = img_to_array(load_img(file)) / 255

	# TODO: validate input
	pred = model.predict(np.expand_dims(x, axis=0))

	print('Input', x)
	print('Output', pred)

	genre = 'metal!' if pred[0][0] < 0.5 else 'not metal'

	return genre, pred[0][0]
