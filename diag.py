import os
path = r'd:\agri\backend\app.py'
with open(path, 'rb') as f:
    data = f.read()
print(f"File size: {len(data)}")
print(f"Find 'register': {data.find(b'register')}")
print(f"Find '@app.post': {data.find(b'@app.post')}")
