import csv

from rest_framework import viewsets,  status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_csv.renderers import CSVRenderer

from .models import Control
from .serializers import ControlSerializer


class ControlViewSet(viewsets.ModelViewSet):
    queryset = Control.objects.all()
    serializer_class = ControlSerializer

    @action(methods=['POST'], detail=False, url_path='upload')
    def upload(self, request):

        for file in request.FILES.values():
            print(file)
            f = file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(f)
            entry_list = []
            for line in reader:
                entry_list.append(line)
            for entry in entry_list:
                Control.objects.create(
                    name=entry['name'], type=entry['type'],
                    maximum_rabi_rate=float(entry['maximum_rabi_rate']),
                    polar_angle=float(entry['polar_angle'])
                )

        return Response("Uploaded", status.HTTP_201_CREATED)

    @action(detail=False, url_path='download', renderer_classes=[CSVRenderer])
    def download(self, request, *args, **kwargs):
        queryset = self.queryset
        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data)

class ControlCSVViewSet(viewsets.ViewSet):
    queryset = Control.objects.all()
    serializer_class = ControlSerializer
    renderer_classes = [CSVRenderer]
    filename = 'controls.csv'

    def list(self, request):
        queryset = self.queryset
        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data)