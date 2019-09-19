from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
	return 'Hello, world'

@app.route('/greet/<name>', methods=['GET'])
def greet(name):
	return 'Hello {}'.format(name)

@app.errorhandler(404)
def error(e):
	return 'Sorry, not found', 404

@app.route('/add_numbers', methods=['POST'])
def add_numbers():
	data = request.form
	# jsonData = request.json
	if 'num1' not in data.keys():
		return 'Missing num1', 400
	if 'num2' not in data.keys():
		return 'Missing num2', 400

	sum = int(data['num1']) + int(data['num2'])
	return jsonify({
		'code': '200',
		'result': sum,
	})
