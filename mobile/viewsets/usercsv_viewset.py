from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from django.db.models import Q
import json
from ..serializers.usercsv_serializer import UserCSVSerializer
import csv
from django.views.generic import View
from django.http import HttpResponse

from ..models.usercsv import Usercsv



class UserCSVViewSet(ModelViewSet):
    queryset = Usercsv.objects.all()
    serializer_class = UserCSVSerializer


class UserCSVSearchView(ListAPIView):
    serializer_class = UserCSVSerializer

    def get_queryset(self):
        search = self.request.query_params.get('q', None)
        if search is not None and search:
            return Usercsv.objects.filter(Q(title__contains=search) | Q(description__contains=search))
        return []

def uploadCSV(ModelViewSet):
    with open('mobile/file/export.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        Usercsv.objects.all().delete()
        for row in reader:
            usercsv = Usercsv(
                title=row.get('title',''),
                description=row.get('description',''),
                image=row.get('image',''),
            )
            usercsv.save()
    response = HttpResponse(json.dumps({"result":"Your CSV FILE has been uploaded successfully"}),content_type='application/json')
    return response


class UserCSVExportView(View):
    serializer_class = UserCSVSerializer

    def get_serializer(self, queryset, many=True):
        return self.serializer_class(
            queryset,
            many=many,
        )

    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="export.csv"'

        serializer = self.get_serializer(
            Usercsv.objects.all(),
            many=True
        )
        header = UserCSVSerializer.Meta.fields

        writer = csv.DictWriter(response, fieldnames=header)
        writer.writeheader()
        for row in serializer.data:
            writer.writerow(row)

        return response
