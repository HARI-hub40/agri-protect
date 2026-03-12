import requests
url = "http://127.0.0.1:8001/predict"
files = {'file': open('d:/agri/red.jpg', 'rb')}
data = {'user_id': '', 'crop': 'Tomato'}
response = requests.post(url, files=files, data=data)
print(response.status_code)
print(response.text)
