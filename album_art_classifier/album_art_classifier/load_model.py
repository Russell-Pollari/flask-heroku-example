from album_art_classifier.AlbumArtClassifier import AlbumArtClassifier


def load_model(path_to_model='trained_models/model.h5'):
	print('Loading model from file system...')
	classifer = AlbumArtClassifier()
	classifer.load_weights(path_to_model)
	return classifer
