import os
import unittest

from unittest import mock
from fastapi.testclient import TestClient

from app.entrypoints.api import client


class TestAPIClient(unittest.TestCase):

    @classmethod
    @mock.patch.dict(os.environ, {"CONFIG_PATH": "./tests/test_config.yaml"}, clear=True)
    def setUpClass(cls):
        cls.client: TestClient = TestClient(client.create_app())

    def test_doc_endpoint(self):
        req = self.client.get('/docs')
        self.assertTrue(req.ok)
