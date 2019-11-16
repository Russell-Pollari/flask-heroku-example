import os
from flask import Flask, request, render_template, jsonify

from album_art_classifier.load_model import load_model

classifer = load_model(from_s3='S3_URL' in os.environ)

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')


@app.route('/predict', methods=['POST'])
def classify_album():
	if request.method == 'POST':
		if 'album' not in request.files:
			return 'No file attached', 400

		file = request.files['album']
		# TODO: check file type and format etc

		genre, pred = classifer.classify_one(file)

		return jsonify({
			'genre': genre
		})


if __name__ == '__main__':
	app.run()
