import requests

file = open('data/sample/metal/0C3puNFNfpDwVHEZNU4Shx.jpg')

response = requests.post('http://localhost:5000/predict', files={ "file": file })

print(response.json())
