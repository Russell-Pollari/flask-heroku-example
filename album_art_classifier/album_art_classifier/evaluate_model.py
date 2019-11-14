from tensorflow.keras.preprocessing.image import ImageDataGenerator


def evaluate_model(model, data_path='data/test'):
	data_gen = ImageDataGenerator(rescale=1 / 255)
	test_generator = data_gen.flow_from_directory(
		data_path,
		target_size=(300, 300),
		class_mode='binary'
	)
	model.evaluate_generator(test_generator, verbose=1)


if __name__ == '__main__':
	print('hi')
