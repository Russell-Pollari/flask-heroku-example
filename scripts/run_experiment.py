import argparse
import tempfile
import math
import mlflow
from tensorflow.keras.callbacks import Callback

from album_art_classifier.model import model
from album_art_classifier.train_model import train_model


class MlFlowCallback(Callback):
	def __init__(self, test_dir=None):
		self.best_val_loss = math.inf

	def on_train_begin(self, logs={}):
		mlflow.log_params(self.params)

	def on_epoch_end(self, epoch, logs={}):
		mlflow.log_metrics({
			'train_acc': logs['acc'],
			'val_acc': logs['val_acc'],
			'train_loss': logs['loss'],
			'val_loss': logs['val_loss']
		}, step=epoch)

		if logs['val_loss'] < self.best_val_loss:
			# TODO: run on test set
			save_name = 'model-chkpt-{}.h5'.format(epoch)
			with tempfile.TemporaryDirectory() as tmpdir:
				self.model.save('{}/{}'.format(tmpdir, save_name))
				mlflow.log_artifact('{}/{}'.format(tmpdir, save_name))


def run_experiment(
	exp_name,
	train_dir='data/train',
	val_dir='data/validate',
	test_dir='data/test',
	model_path=None,
	epochs=10,
	batch_size=16
):
	experiment_id = mlflow.set_experiment(exp_name)

	with mlflow.start_run(experiment_id=experiment_id):
		train_model(
			model,
			model_path=model_path,
			epochs=epochs,
			batch_size=batch_size,
			train_dir=train_dir,
			val_dir=val_dir,
			callbacks=[MlFlowCallback()]
		)


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('name')
	parser.add_argument('--train_dir')
	parser.add_argument('--test_dir')
	parser.add_argument('--val_dir')
	parser.add_argument('--model_path')
	parser.add_argument('--epochs', type=int)
	parser.add_argument('--batch_size', type=int)

	args = parser.parse_args()
	kwargs = vars(args)
	name = kwargs.pop('name')
	run_experiment(name, **kwargs)
