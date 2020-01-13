import csv

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

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

        #  file = request.FILES['file'].read().decode('utf-8').splitlines()
        #
        # # for file in request.FILES:
        # #     pass
        # # data = csv.DictReader(file)
        # print(f'file name: {file}')
        #
        # reader = csv.DictReader(file)
        # entry_list = []
        # for line in reader:
        #     entry_list.append(line)
        #
        # for entry in entry_list:
        #     print(
        #         f'name: {entry["name"]}, type: {entry["type"]}, max_rabi: {entry["maximum_rabi_rate"]}, polar_angle: {entry["polar_angle"]}')
        # # for entry in entry_list:
        # #     Control.objects.create(name=entry['name'], type=entry['type'], maximum_rabi_rate=entry['maximum_rabi_rate'],
        # #                           polar_angle=entry['polar_angle'])

        return Response("Done", status.HTTP_201_CREATED)

# class ControlUploadView(views.APIView):
#     parser_classes = [FileUploadParser]
#
#     def put(self, request, format='csv'):
#         file = request.FILES['filename']
#
#         print(f'file name: {file.filename}')
#
#         return Response(file.filename, status.HTTP_201_CREATED)