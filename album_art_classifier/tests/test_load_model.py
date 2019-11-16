import os
import pytest

from album_art_classifier.load_model import load_model


@pytest.mark.skipif('S3_URL' not in os.environ, reason="No s3 url")
def test_s3():
	classifier = load_model(from_s3=True)

	assert classifier is not None
