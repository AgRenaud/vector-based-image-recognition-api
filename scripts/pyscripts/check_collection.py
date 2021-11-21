import requests
import json
import sys

qdrant_url = sys.argv[1]
collection_name = sys.argv[2]

req = requests.get(f"{qdrant_url}/collections/{collection_name}")

if req.status_code==200:
    data = req.json()
    result = data['result']
    config = result['config']
    params = config['params']
    print("--------")
    print(f"NAME: {collection_name}")
    print(f"VECTORS: {result['vectors_count']}")
    print(f"VECTOR_SIZE: {params['vector_size']}\tDISTANCE: {params['distance']}")
    print("--------")
else:
    print(f"Can't check collection {collection_name}")
