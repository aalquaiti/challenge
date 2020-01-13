from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from control import models, serializers

class ControlAPI(TestCase):
    """Test all functionality provided by control api"""

    def setUp(self):
        self.client = APIClient()


    def test_create_success(self):
        """
        Tests Control can be created successfully given right format
        """
        data = '''
            {
                "data": {
                    "type": "Control",
                    "id": null,
                    "attributes": {
                        "name": "Abdullah",
                        "type": "CinSK",
                        "maximum_rabi_rate": 12.45,
                        "polar_angle": 0.5
                    }
                }
            }
        '''
        response = self.client.post('/api/control/', data, format='vnd.api+json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # def test_list_all(self):
    #
    #
    # def test_list_specific_control(self):
    #
    # def test_update_control(self):
    #
    # def test_delete_control(self):
    #
    # def test_bulk_upload_controls(self):
    #
    # def test_download_control_csv(self):
