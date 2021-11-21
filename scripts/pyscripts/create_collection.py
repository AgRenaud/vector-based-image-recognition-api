import requests
import json
import sys

qdrant_url = sys.argv[1]
collection_name = sys.argv[2]
distance = sys.argv[3]
vector_size = sys.argv[4]

payload = {
    "create_collection": {
        "name": str(collection_name),
        "distance": str(distance),
        "vector_size": int(vector_size)
    }
}

req = requests.post(f"{qdrant_url}/collections", json=payload)

print(f" - Create collection {collection_name}:\t{req.status_code}")
