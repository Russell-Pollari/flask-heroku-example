import os
import pytest

from album_art_classifier.AlbumArtClassifier import AlbumArtClassifier

data_directory = 'data/sample'


@pytest.mark.skipif(not os.path.exists(data_directory), reason="No sample data to train on")  # noqa E501
def test_train(tmp_path):
	model_path = tmp_path / 'test_model.h5'

	classifier = AlbumArtClassifier()
	classifier.fit_from_directory(data_directory, model_path=model_path)

	assert os.path.exists(model_path)
