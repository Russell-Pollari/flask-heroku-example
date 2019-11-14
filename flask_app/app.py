from flask import Flask, request, render_template, jsonify
from tensorflow.keras.models import load_model

from album_art_classifier.predict_model import predict

# TODO: Load model from model registry
print('Loading model...')
model = load_model('trained_models/model.h5')

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')


@app.route('/predict', methods=['POST'])
def classify_album():
	if request.method == 'POST':
		if 'album' not in request.files:
			return 'No file found', 400

		file = request.files['album']

		# TODO: check file type and format etc
		genre, pred = predict(model, file)

		return jsonify({'genre': genre})


if __name__ == '__main__':
	app.run()
