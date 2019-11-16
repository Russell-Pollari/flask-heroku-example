import os

from album_art_classifier.AlbumArtClassifier import AlbumArtClassifier


def test_predict():
	path_to_current_file = os.path.realpath(__file__)
	current_directory = os.path.dirname(path_to_current_file)
	path_to_test_image = os.path.join(current_directory, "test-image.jpg")

	classifier = AlbumArtClassifier()

	genre, pred = classifier.classify_one(path_to_test_image)

	assert genre in ['metal', 'not_metal']
	assert pred is not None
