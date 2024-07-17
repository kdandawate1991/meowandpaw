import requests
import logging

logger = logging.getLogger(__name__)


class Crud:
    def __init__(self):
        self.base_url = 'https://petstore.swagger.io/v2'  # Ideally i would store this in ssm or some other vault
        # self.header = header  #  Not needed for demo but in real scenarios we will need one

    def get_resource(self, endpoint, params=None):
        url = self.base_url + endpoint
        response = requests.get(url, params=params, verify=False)
        resp_data = None
        if response.status_code == 200:
            resp_data = response.json()
        logger.debug(f'endpoint = {endpoint}\nresponse = {resp_data}')
        return response

    def create_resource(self, endpoint, payload=None, files=None):
        url = self.base_url + endpoint
        response = requests.post(url, json=payload, files=files, verify=False)
        resp_data = None
        if response.status_code == 200:
            resp_data = response.json()
        logger.debug(f'endpoint = {endpoint}\nresponse = {resp_data}')
        return response

    def update_resource(self, endpoint, payload=None):
        url = self.base_url + endpoint
        response = requests.patch(url, json=payload, verify=False)
        resp_data = None
        if response.status_code == 200:
            resp_data = response.json()
        logger.debug(f'endpoint = {endpoint}\nresponse = {resp_data}')
        return response

    def delete_resource(self, endpoint):
        url = self.base_url + endpoint
        response = requests.delete(url, verify=False)
        resp_data = None
        if response.status_code == 200:
            resp_data = response.json()
        logger.debug(f'endpoint = {endpoint}\nresponse = {resp_data}')
        return response

