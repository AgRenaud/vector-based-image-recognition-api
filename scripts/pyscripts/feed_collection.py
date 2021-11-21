import requests
import json
import sys
import os


qdrant_url = sys.argv[1]
collection_name = sys.argv[2]
points_folder = sys.argv[3]

def read_json(path: str) -> dict:
    with open(path, 'rb') as f:
        data = json.load(f)
    return data

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

json_files = [os.path.join(points_folder, file) for file in os.listdir(points_folder) if file.endswith('.json')]

for chk in chunks(json_files, 25):
    points = [read_json(file) for file in chk]
    payload = {
        "upsert_points": {
            "points": points
        }
    }

    req = requests.post(f"{qdrant_url}/collections/{collection_name}", json=payload)

    if req.status_code == 200:
        res = req.json()
        print(f" - Upsert {len(points)} points:\t{res['result']['status']}")
    else:
        print(f"[WARNING] {req.status_code}")
        print(type(points))
        print(points[0])
