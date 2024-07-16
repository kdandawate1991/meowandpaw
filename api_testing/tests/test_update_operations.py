import pytest
import logging
from api_testing.api.pets import Pets

logger = logging.getLogger(__name__)


@pytest.mark.api  # marker to run just api tests if needed
class TestPetsUpdateOperations:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.pets = Pets()

    def test_update_pet(self):
        id_to_update = 10
        payload = {
            "name": "kavita",
            "status": "in testing"
        }
        response = self.pets.update_pet_by_id(id_to_update, payload=payload)
        assert response.status_code == 200, f"expected 200 status code, got {response.status_code}"

        assert response.json()['name'] == payload['name'], (f"Value not updated correctly, expected: {payload['name']},"
                                                            f" actual: {response.json()['name']}")
        assert response.json()['status'] == payload['status'], (f"value not updated correctly,"
                                                                f" expected: {payload['status']},"
                                                                f" actual: {response.json()['status']}")

