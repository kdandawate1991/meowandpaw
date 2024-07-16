import pytest
import logging
from api_testing.api.pets import Pets

logger = logging.getLogger(__name__)

PAYLOAD_1 = {
    "id": 0,
    "category": {
        "id": 0,
        "name": "string"
    },
    "name": "doggie",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
            "id": 0,
            "name": "string"
        }
    ],
    "status": "available"
}

PAYLOAD_2 = {
    "id": 25,
    "status": "available"
}

PAYLOAD_3 = {}

NEGATIVE_PAYLOAD_1 = {
    "id": 0,
    "status": 1
}


@pytest.mark.api  # marker to run just api tests if needed
class TestPetsCreateOperations:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.pets = Pets()

    @pytest.mark.parametrize('payload', [PAYLOAD_1, PAYLOAD_2, PAYLOAD_3])
    def test_create_pet(self, payload):
        """Add a new pet to the store with different payloads"""
        response = self.pets.create_new_pet(payload=payload)
        assert response.status_code == 200, f"expected 200 response code , received {response.status_code}"

    def test_create_negative_pet(self):
        response = self.pets.create_new_pet(payload=PAYLOAD_3)
        assert response.status_code == 405, (f"expected 405 response code as int provided for status insetad of string"
                                             f" , received {response.status_code}")