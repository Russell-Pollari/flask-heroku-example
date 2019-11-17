import os
import math
from tensorflow.keras.preprocessing.image import ImageDataGenerator


def count_files(dir):
	total = 0
	for root, dirs, files in os.walk(dir):
		total += len(files)
	return total


def train_model(
	model,
	epochs=10,
	batch_size=16,
	callbacks=[],
	model_path=None,
	train_dir='data/train',
	val_dir='data/validate'
):
	model.compile(
		loss='binary_crossentropy',
		optimizer='rmsprop',
		metrics=['acc']
	)

	data_gen = ImageDataGenerator(rescale=1 / 255)

	train_generator = data_gen.flow_from_directory(
		train_dir,
		target_size=(300, 300),
		class_mode='binary',
	)

	validation_generator = data_gen.flow_from_directory(
		val_dir,
		target_size=(300, 300),
		class_mode='binary',
	)

	train_steps = math.floor(count_files(train_dir) / batch_size)
	val_steps = math.floor(count_files(val_dir) / batch_size)

	model.fit_generator(
		train_generator,
		steps_per_epoch=train_steps,
		epochs=epochs,
		verbose=1,
		validation_data=validation_generator,
		validation_steps=val_steps,
		callbacks=callbacks
	)

	if model_path is not None:
		print('Saving model as', model_path)
		model.save(model_path)

	return model
