from flask import Flask, request, render_template
from utils import is_number

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
	return render_template('home.html')

@app.route('/greet/<name>', methods=['GET'])
def greet(name):
	return 'Hello {}'.format(name)

@app.route('/add_numbers', methods=['POST'])
def add_numbers():
	data = request.form

	if 'num1' not in data.keys():
		return 'Missing num1', 400
	if 'num2' not in data.keys():
		return 'Missing num2', 400

	num1 = data['num1']
	num2 = data['num2']

	if not is_number(num1):
		return 'Num1 is invalid', 400
	if not is_number(num2):
		return 'Num2 is invalid', 400

	sum = float(num1) + float(num2)

	return render_template('home.html', result=sum, num1=num1, num2=num2)

@app.errorhandler(404)
def error(e):
	return 'Sorry, not found', 404

if __name__ == '__main__':
	app.run();
