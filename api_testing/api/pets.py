import logging
from api_testing.api.crud import Crud
logger = logging.getLogger(__name__)


class Pets(Crud):
    def create_new_pet(self, payload):
        """:param payload: dict: payload that needs to be passed to create a pet"""
        endpoint = '/pet'
        return self.create_resource(endpoint, payload=payload)

    def get_pet_by_id(self, pet_id):
        """param pet_id int: specific pet id to be found"""
        endpoint = f'/pet/{pet_id}'
        return self.get_resource(endpoint)

    def get_pet_by_status(self, status):
        """param status str: pet status to be found. valid options are (available, pending, sold)"""
        endpoint = f'/pet/findByStatus/'
        params = {'status': status}
        return self.get_resource(endpoint, params)

    def update_pet(self, payload):
        """:param payload: dict: payload that needs to be passed to create a pet"""
        endpoint = f'/pet'
        return self.update_resource(endpoint, payload=payload)

    def update_pet_by_id(self, pet_id, payload):
        """ :param pet_id: int: specific pet id to be found
            :param payload: dict: payload that needs to be passed to create a pet
        """
        endpoint = f'/pet/{pet_id}'
        return self.update_resource(endpoint, payload=payload)

    def upload_pet_image(self, pet_id, image_path):
        """ :param pet_id: int: specific pet id to be found
            :param image_path: str: path to image to be uploaded
        """
        endpoint = f'/pet/{pet_id}/uploadImage'
        files = {'file': open(image_path, 'rb')}
        return self.create_resource(endpoint, files=files)

    def delete_pet_by_id(self, pet_id):
        endpoint = f'/pet/{pet_id}'
        return self.delete_resource(endpoint)
