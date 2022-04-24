import json
import requests
import logging

from numpy import array
from qdrant_client import QdrantClient


class QdrantGateway:

    _logger = logging.getLogger(__name__)

    def __init__(self, qdrant_url: str, qdrant_port: str, collection_name: str):
        self._client = QdrantClient(host=qdrant_url, port=qdrant_port)
        self.collection = collection_name

    def search(self, query_vector: array):

        search_result = self._client.search(
            collection_name=self.collection,
            query_vector=query_vector,
            query_filter=None, # Don't use any filters for now, search across all indexed points
            append_payload=True, # Also return a stored payload for found points
            top=5,  # Return 5 closest points
        )

        #
        search_result = [
            {"class": x[1]["class"][0], "score": x[0].dict()["score"]}
            for x in search_result
        ]

        return search_result
