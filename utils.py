def is_number(num):
	try:
		float(num)
		return True
	except ValueError:
		return False
