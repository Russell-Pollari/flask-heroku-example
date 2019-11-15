import os
from album_art_classifier import AlbumArtClassifier


def test_train(tmp_path):
	test_directory = 'data/sample'
	save_path = tmp_path / 'test_model.h5'

	classifier = AlbumArtClassifier()
	classifier.fit_from_directory(test_directory, save_path)

	assert os.path.exists(save_path)
