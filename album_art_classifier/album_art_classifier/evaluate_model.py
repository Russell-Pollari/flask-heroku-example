import os
import math
from tensorflow.keras.preprocessing.image import ImageDataGenerator


def count_files(dir):
	total = 0
	for root, dirs, files in os.walk(dir):
		total += len(files)
	return total


def evaluate_model(model, test_dir='data/test'):
	data_gen = ImageDataGenerator(rescale=1. / 255)

	test_generator = data_gen.flow_from_directory(
		test_dir,
		target_size=(300, 300),
		class_mode='binary',
	)

	test_steps = math.floor(count_files(test_dir))

	metrics = model.evaluate_generator(
		test_generator,
		steps=test_steps,
		verbose=1,
	)

	return metrics
