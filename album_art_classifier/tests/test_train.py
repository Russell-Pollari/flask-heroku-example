import os
import pytest

from album_art_classifier import AlbumArtClassifier

data_directory = 'data/sample'


@pytest.mark.skipif(not os.path.exists(data_directory), reason="No sample data to train on")  # noqa E501
def test_train(tmp_path):
	save_path = tmp_path / 'test_model.h5'

	classifier = AlbumArtClassifier()
	classifier.fit_from_directory(data_directory, save_path)

	assert os.path.exists(save_path)
