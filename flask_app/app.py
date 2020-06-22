from flask import Flask, request, render_template, jsonify

from album_art_classifier import AlbumArtClassifier

classifer = AlbumArtClassifier()
classifer.load_weights('mlruns/7/365eed74f779486aa068428eac081f29/artifacts/model-chkpt-0.h5') # noqa

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
