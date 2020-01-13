from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from control import models, serializers

class ControlAPI(TestCase):
    """Test all functionality provided by control api"""

    def setUp(self):
        self.client = APIClient()


    def test_create_new_control(self):
        pass

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
