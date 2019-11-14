# Basic Flask app for Heroku

Minimal working Flask app hosting an image classifier for Heroku.  

Live example here:
https://sm-flask-heroku-tutorial.herokuapp.com/


## Deploying:
1. Create heroku account and install heroku CLI: https://devcenter.heroku.com/articles/heroku-cli#download-and-install
2. `$ heroku create <app_name>`
3. `$ git push heroku master`


## Directory structure
```
├── .circleci/
|   └── config.yml // config for circleci
├── album_art_classifier // package containing ML model
|		├── album_art_classifier // source code for ML model
|		├── tests // tests for ML model
|		└── setup.py // make this a python package
├── flask_app/
|		├── templates // html templates
|		└── app.py // Flask app
├── trained_models/ // saved ML models
|		└── model.h5
├── .gitignore // files and folders to keep out of version control
├── Procfile // Instructions for Heroku
├── README.md // you're reading it :)
├── requirements.txt // tells Heroku what to install
├── runtime.txt // specifies the python version for Heroku
└── train.py // script to train ML model on training data
```

## Development

(Recommended) Setup up virtual environment https://virtualenv.pypa.io/en/latest/  
`$ virtualenv venv`  
`$ source venv/bin/activate`

Install dependencies:  
`$ pip install -r requirements.txt`

To ensure app runs in debug mode set `FLASK_ENV` envioronment variable before running:  
`$ export FLASK_ENV=development`

To run app locally (starts server on localhost:5000)  
`$ python flask_app/app.py`
