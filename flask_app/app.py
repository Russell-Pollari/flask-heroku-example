from flask import Flask, request, render_template, jsonify

from album_art_classifier import AlbumArtClassifier

# TODO: Load model from model registry
print('Loading model...')
classifer = AlbumArtClassifier()
classifer.load_weights('trained_models/model.h5')

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
