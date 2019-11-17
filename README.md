# Album art classifier

Classify an album as metal or not metal based on it's album art.
This repo contains the ML package as well as a simple Flask app to host.

Live example here: https://sm-flask-heroku-tutorial.herokuapp.com/

## Directory structure
```
├── .circleci/
|   └── config.yml // config for circleci
├── album_art_classifier // package containing ML model
|   ├── album_art_classifier // source code for ML model
|   |   ├── __init__.py
|   |   ├── AlbumArtClassifier.py
|   |   ├── load_model.py
|   |   ├── model.py
|   |   └── train_model.py
|   ├── tests // tests for ML package
|   └── setup.py // Make this a python package
├── flask_app
|   ├── templates // html templates
|   |   └── index.html
|   └── app.py // Flask app
├── scripts
|   ├── download_data.py // fetch data from remote storage
|   └── run_experiment.py // run an mlflow experiment
├── trained_models // saved ML models (for local development)
|   └── .gitignore // don't commit models to version control
├── .flake8 // linter config
├── .gitignore
├── Procfile // deployment instructions for Heroku
├── README.md // you're reading it :)
├── requirements.txt // pip requirements
└── runtime.txt // specify the Python version for Heroku
```

## Development

### Set up enviornment
(Recommended) Setup up virtual environment https://virtualenv.pypa.io/en/latest/  
`$ virtualenv venv`  
`$ source venv/bin/activate`

Install dependencies:  
`$ pip install -r requirements.txt`


### Training/experiments
#### Download data  
`$ python scripts/download_data.py`  
Download the dataset from S3 and extract it into the root directory:
```
├── data
    ├── sample
    |   ├── metal/
    |   └── not-metal/
    ├── test
    |   ├── metal/
    |   └── not-metal/
    ├── train
    |   ├── metal/
    |   └── not-metal/
    └── validate
        ├── metal/
        └── not-metal/
```

#### Run experiment
```
$ python scripts/run_experiment.py experiment_name \
	--train_dir data/train
	--val_dir data/validate
	--model_path trained_models/model.h5
	--epochs 10
	--batch_size 32
```

#### View experiments
`$ mlflow ui`


## Running Flask app locally

To ensure app runs in debug mode set `FLASK_ENV` envioronment variable before running:  
`$ export FLASK_ENV=development`

To run app locally (starts server on localhost:8000)  
`$ gunicorn flask_app.app:app`


## Deploying:

1. Create heroku account and install heroku CLI: https://devcenter.heroku.com/articles/heroku-cli#download-and-install
2. `$ heroku create <app_name>`
3. Set `S3_URL` env variable (points to saved weights)  
`$ heroku config:set S3_URL=<url>`  
4. Deploy: `$ git push heroku master`
