# Created by: Aymen Al-Quaiti
# For QCTRL Backend Challenge
# January  2020
"""
Contains Rest Services provided by Control App
"""

import csv, logging
from rest_framework import viewsets,  status
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework_csv.renderers import CSVRenderer
from .models import Control
from .serializers import ControlSerializer

logger = logging.getLogger(__name__)

class ControlViewSet(viewsets.ModelViewSet):
    """
    Main API Service that currently handle all API interactions. As this is a ModelViewSet, by default it handles
    five of the challenge requirements, namely:
    1. Creating a controller
    2. Listing a controller (paginated at five for each page)
    3. Retrieve a specific controller
    4. Update a specific controller
    5. Delete a specific controller
    All these services follows the JSON API specification

    In addition, two actions has been added for:
    6. Uploading a CSV for bulk creation
    7. Downloading a CSV file contain list of all controllers
    """
    queryset = Control.objects.all()
    serializer_class = ControlSerializer

    @action(methods=['POST'], detail=False, url_path='upload')
    def upload(self, request):
        """
        Upload a CSV file, parse it and create new controllers accordingly

        args:
            request: HTTP request to process
        """

        # For each file uploaded
        for file in request.FILES.values():
            logger.info("Processing uploaded file")

            # Read file as string
            f = file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(f)
            entry_list = []
            for line in reader:
                entry_list.append(line)

            # Process each entry
            try:
                for entry in entry_list:
                    Control.objects.create(
                        name=entry['name'], type=entry['type'],
                        maximum_rabi_rate=float(entry['maximum_rabi_rate']),
                        polar_angle=float(entry['polar_angle'])
                    )
            except ValidationError as e:
                return Response(f"Error processing file(s). {e} ", status.HTTP_400_BAD_REQUEST)

        return Response("File(s) processed successfully", status.HTTP_201_CREATED)

    @action(detail=False, url_path='download', renderer_classes=[CSVRenderer])
    def download(self, request):
        """
        Download all Control entries in CSV format

        args:
            request: HTTP Request
        """
        queryset = self.queryset
        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data)

