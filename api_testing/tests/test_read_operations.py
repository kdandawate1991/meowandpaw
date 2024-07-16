import pytest
import logging
from api_testing.api.pets import Pets

logger = logging.getLogger(__name__)


@pytest.mark.api  # marker to run just api tests if needed
class TestPetsReadOperations:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.pets = Pets()

    @pytest.mark.parametrize('status', ['available', 'pending', 'sold'])
    def test_get_pet(self, status):
        """
        Test to retrieve pet by single status
        1. verify response code is 200
        2. verify if status of each pet returned matches the status in query
        3. verify if all ids are unique
        4. validate if pet can be found by id
        """
        logger.info(f"Performing test for status {status}")
        response = self.pets.get_pet_by_status(status)

        # validate response code
        assert response.status_code == 200, f"expected status code 200, received {response.status_code}"

        pets_in_store = response.json()
        id_list = []

        # validations for status
        for pet in pets_in_store:
            assert pet['status'] == status, f"status from api should match the queried status"
            id_list.append(pet['id'])

        # validation for id uniqueness
        assert len(id_list) == len(set(id_list)), "All ids should be unique, found duplicate ids"

    def test_get_pet_by_multiple_status_and_id(self):
        """
            Test to retrieve pet by multiple status's and also by id
            1. verify response code is 200
            2. verify if all ids are unique
        """
        logger.info(f"Performing test for all status's available, sold and pending")
        response = self.pets.get_pet_by_status(['available', 'sold', 'pending'])
        # validate response code
        assert response.status_code == 200, f"expected status code 200, received {response.status_code}"

        pets_in_store = response.json()
        id_list = []
        # validations for status
        for pet in pets_in_store:
            id_list.append(pet['id'])

        # validation for id uniqueness
        assert len(id_list) == len(set(id_list)), "All ids should be unique, found duplicate ids"

        # verify if we can get pet by some id
        id_to_check = id_list[0]
        response = self.pets.get_pet_by_id(id_to_check)
        assert response.status_code == 200, f"expected status code 200, received {response.status_code}"

    def test_get_pet_invalid_status(self):
        """
        Tests to verify if we get correct error codes for invalid status
        :return:
        """
        logger.info(f"Performing test for invalid status")
        response = self.pets.get_pet_by_status('testnegative')
        assert response.status_code == 400, f"expected status code 400, received {response.status_code}"

    def test_get_pet_nonexistent_id(self):
        """Test to verify if we get correct error codes for non-existent id"""
        logger.info(f"Performing test for non-existent id")
        #  validate correct error code is returned on providing invalid value
        response = self.pets.get_pet_by_id('nonexistentid')
        assert response.status_code == 400, f"expected status code 400, received {response.status_code}"

        # validate error code when negative value provided
        response = self.pets.get_pet_by_id(-123485468888778)
        assert response.status_code == 400, f"expected status code 400, received {response.status_code}"

        # validate error code when correct value provided but pet does not exists
        response = self.pets.get_pet_by_id(111111111111111111)
        assert response.status_code == 404, f"expected status code 404, received {response.status_code}"
