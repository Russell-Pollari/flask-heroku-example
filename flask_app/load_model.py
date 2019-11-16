import tempfile
import wget
import os

from album_art_classifier.AlbumArtClassifier import AlbumArtClassifier


def load_model(from_s3=True):
	classifer = AlbumArtClassifier()

	if from_s3:
		s3_url = os.getenv('S3_URL')
		with tempfile.TemporaryDirectory() as tmpdir:
			print('Fetching weights from S3', s3_url)
			wget.download(s3_url, '{}/weights.h5'.format(tmpdir))

			print('Loading weights...')
			classifer.load_weights('{}/weights.h5'.format(tmpdir))
	else:
		print('Loading model from file system')
		classifer.load_weights('trained_models/model.h5')

	return classifer
