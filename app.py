import os
import numpy as np
from flask import Flask, request, render_template, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array

# TODO: Load model from remote storage
print('Loading model...');
model = load_model('trained_models/model.h5')

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
	if request.method == 'POST':
		if 'album' not in request.files:
			return 'No file found', 400

		file = request.files['album']
		# TODO: check file type and format etc
		try:
			x = img_to_array(load_img(file)) / 256
		except:
			return 'Invalid input', 400

		# TODO: validate input
		pred = model.predict(np.expand_dims(x, axis=0))

		print('Input', x)
		print('Output', pred);

		result = pred[0][0]
		genre = 'metal!' if pred[0][0] < 0.5 else 'not metal'

		return jsonify({ 'genre': genre });


if __name__ == '__main__':
	app.run()
