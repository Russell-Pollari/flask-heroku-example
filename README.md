# Album art classifier

Classify an album as metal or not metal based on it's album art.
This repo is contains the ML package as well as a simple Flask app to host.
Work in progress to demonstrate best practices

Live example here: https://sm-flask-heroku-tutorial.herokuapp.com/

## Directory structure
```
├── .circleci/
|   └── config.yml // config for circleci
├── album_art_classifier // package containing ML model
|   ├── album_art_classifier // source code for ML model
|   |   ├── __init__.py
|   |   ├── AlbumArtClassifier.py
|   |   ├── model.py
|   |   └── train_model.py
|   ├── tests // tests for ML model
|   └── setup.py // makes this a python package
├── flask_app
|   ├── templates // html templates
|   |   └── index.html
|   └── app.py // Flask app
├── scripts
|   └── download_data.py // Flask app
├── trained_models // saved ML models
├── .flake8 // linter config
├── .gitignore // files and folders to keep out of version control
├── Procfile // Instructions for Heroku
├── README.md // you're reading it :)
├── requirements.txt // tells Heroku what to install
├── runtime.txt // specifies the python version for Heroku
```

## Development

### set up enviornment
(Recommended) Setup up virtual environment https://virtualenv.pypa.io/en/latest/  
`$ virtualenv venv`  
`$ source venv/bin/activate`

Install dependencies:  
`$ pip install -r requirements.txt`


### Training model
Download data  
`$ python scripts/downlaod_data.py`  

Train model  
`$ python album_art_classifier/album_art_classifier/train_model.py --save_path trained_models/model.h5 --data_folder data/train`


### Running Flask app

To ensure app runs in debug mode set `FLASK_ENV` envioronment variable before running:  
`$ export FLASK_ENV=development`

To run app locally (starts server on localhost:5000)  
`$ python flask_app/app.py`


## Deploying:

1. Create heroku account and install heroku CLI: https://devcenter.heroku.com/articles/heroku-cli#download-and-install
2. `$ heroku create <app_name>`
3. Set `S3_URL` env variable (points to saved weights)  
`$ heroku config:set S3_URL=<url>`  
4. Deploy: `$ git push heroku master`
