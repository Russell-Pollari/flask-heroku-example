# Basic Flask app for Heroku

Minimal working Flask app for Heroku.  
Adds two numbers (wow!).

Live example here:
https://sm-flask-heroku-tutorial.herokuapp.com/


## Deploying:
1. Create heroku account and install heroku CLI: https://devcenter.heroku.com/articles/heroku-cli#download-and-install
2. `$ heroku create <app_name>`
3. `$ git push heroku master`


## Directory structure
```
├── templates // html templates that can be used with render_template
|   └── home.html
├── .gitignore // files and folders to keep out of version control
├── app.py // Flask app and routes
├── Procfile // tells Heroku what to run
├── requirements.txt // tells Heroku what to install
├── runtime.txt // specifies the python version for Heroku
└── utils.py // utility functions
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
`$ flask run`
