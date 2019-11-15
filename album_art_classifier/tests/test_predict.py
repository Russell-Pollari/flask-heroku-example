from album_art_classifier import AlbumArtClassifier


def test_predict():
	test_image_path = 'data/sample/metal/0C3puNFNfpDwVHEZNU4Shx.jpg'

	classifier = AlbumArtClassifier()
	classifier.load_weights('trained_models/model.h5')

	genre, pred = classifier.classify_one(test_image_path)

	assert genre in ['metal', 'not_metal']
	assert pred is not None
