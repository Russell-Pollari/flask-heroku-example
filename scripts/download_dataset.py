import os
import wget
import tarfile


def download_dataset(data_url, save_as='data/albums.tar.gz'):
	if not os.path.exists(save_as):
		wget.download(data_url, save_as)

	with tarfile.open(save_as) as tar:
		tar.extractall()


if __name__ == '__main__':
	data_url = 'https://album-art-classifier.s3-us-west-2.amazonaws.com/album-art.tar.gz'  # noqa: E501
	download_dataset(data_url)
