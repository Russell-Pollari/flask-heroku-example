from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array

from model import model

TRAIN_PATH = 'data/train'
TEST_PATH = 'data/test'
SAVE_PATH = 'trained_models/model.h5';

# TODO: set seed

def train_model(model, save_path, data_path):
	model.compile(
		loss='binary_crossentropy',
		optimizer='rmsprop',
		metrics=['accuracy']
	)

	data_gen = ImageDataGenerator(rescale=1./255)

	train_generator = data_gen.flow_from_directory(data_path,
		target_size=(300, 300),
		class_mode='binary'
	)

	model.fit_generator(train_generator,
		steps_per_epoch=20,
		epochs=2,
		verbose=1
	)

	print('Saving model as', save_path)
	model.save(save_path);


def evaluate_model(model, data_path='data/test'):
	data_gen = ImageDataGenerator(rescale=1./255)
	test_generator = data_gen.flow_from_directory(data_path,
		target_size=(300, 300),
		class_mode='binary'
	)
	model.evaluate_generator(test_generator, verbose=1)


if __name__ == '__main__':
	print('Training model...')
	train_model(model, save_path=SAVE_PATH, data_path=TRAIN_PATH)

	# print('Evaulating model')
	# evaluate_model(model, data_path=TEST_PATH)
