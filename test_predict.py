import requests

url = "http://127.0.0.1:8001/predict"
file_path = "D:/agri/frontend/assets/agridetect.ico"
files = {'file': open(file_path, 'rb')}
data = {'user_id': '', 'crop': 'Tomato'}

try:
    response = requests.post(url, files=files, data=data)
    print(response.status_code)
    print(response.text)
except Exception as e:
    print(e)
