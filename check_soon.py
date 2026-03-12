import json
import os

def find_coming_soon(data, path=""):
    if isinstance(data, dict):
        for k, v in data.items():
            find_coming_soon(v, f"{path}.{k}")
    elif isinstance(data, list):
        for i, v in enumerate(data):
            find_coming_soon(v, f"{path}[{i}]")
    elif isinstance(data, str):
        if "Coming Soon" in data:
            print(f"FOUND: {path} = {data}")

files = [
    r"d:\agri\backend\crop_diseases_db.json",
    r"d:\agri\backend\local_treatments.json",
    r"d:\agri\backend\treatments.json",
    r"d:\agri\backend\prices.json",
]

for f in files:
    if os.path.exists(f):
        print(f"Checking {f}...")
        with open(f, 'r', encoding='utf-8') as jf:
            try:
                data = json.load(jf)
                find_coming_soon(data)
            except Exception as e:
                print(f"Error reading {f}: {e}")
