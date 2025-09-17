from unittest import TestCase
import requests
from .setup import Setup


class General(TestCase):
    def test_is_healthy(self):
        response = requests.get("http://localhost:8000/health")
        Setup.get_all_prompts()

        assert response.status_code == 200
        json = response.json()
        assert json == {
            "status": "ok"
        }
