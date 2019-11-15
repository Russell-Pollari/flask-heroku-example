import argparse
from tensorflow.keras.preprocessing.image import ImageDataGenerator

from album_art_classifier.model import model


def train_model(
	model,
	save_path='trained_models/model.h5',
	data_folder='data/train',
):
	model.compile(
		loss='binary_crossentropy',
		optimizer='rmsprop',
		metrics=['accuracy']
	)

	data_gen = ImageDataGenerator(rescale=1 / 255)

	train_generator = data_gen.flow_from_directory(
		data_folder,
		target_size=(300, 300),
		class_mode='binary'
	)

	model.fit_generator(
		train_generator,
		steps_per_epoch=20,
		epochs=2,
		verbose=1
	)

	print('Saving model as', save_path)
	model.save(save_path)

	return model


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--data_folder')
	parser.add_argument('--save_path')
	args = parser.parse_args()

	print('Training model on ', args.data_folder)
	train_model(model, save_path=args.save_path, data_folder=args.data_folder)
