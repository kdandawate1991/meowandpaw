import pytest
import logging
from api_testing.api.pets import Pets

logger = logging.getLogger(__name__)


ID_TO_DELETE = 10


@pytest.mark.api  # marker to run just api tests if needed
class TestPetsDeleteOperations:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.pets = Pets()
        # create a pet which we want to delete in the test.
        self.pets.create_new_pet(payload={"id": ID_TO_DELETE, "status": "available"})
        yield
        # Revert to original state by creating the pet with same if that we deleted
        self.pets.create_new_pet(payload={"id": ID_TO_DELETE, "status": "available"})

    def test_delete_operations(self):
        """Test to verify the deletion of a pet
        1. Validate response code after deletion
        2. Validate if correct error code received when trying to READ the deleted pet
        3. Try to delete non existent id and see if correct error code is received
        """
        logger.info(f"deleting id {ID_TO_DELETE}")
        response = self.pets.delete_pet_by_id(ID_TO_DELETE)
        assert response.status_code == 200, f"expected 200 response code, received {response.status_code}"

        #  Make sure the pet with given id is actuallyd eleted by trying to READ it
        response = self.pets.get_pet_by_id(ID_TO_DELETE)
        assert response.status_code == 404, f"expected 404 response code, received {response.status_code}"

        response = self.pets.delete_pet_by_id(ID_TO_DELETE)
        assert response.status_code == 404, f"expected 404 response code, received {response.status_code}"
