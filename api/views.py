import csv
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from .serializers import DealSerializer


class Home(APIView):
    parser_classes = [MultiPartParser]

    def get(self, request):
        return Response({'is_this': 'working?'}, status=200)

    def post(self, request, format=None):
        content_type = request.content_type.split(';')[0].strip()

        if content_type == 'text/csv':
            csv_table = request.data
            return Response(csv_table, status=200)

        elif content_type == 'multipart/form-data':
            fh = request.data.get('file', None)
            csv_table = self.parse(fh)
            serializer = DealSerializer(data=csv_table)
            if serializer.is_valid():
                serializer.save()
            return Response(csv_table, status=200)
        else:
            return Response(None, status=415)

        return Response(serializer.errors, status=400)


    def parse(self, stream, media_type=None, parser_context=None):
        charset = 'utf-8'
        txt = list(csv.reader(stream.read().decode(charset).splitlines()))
        csv_table = []
        for obj in txt[1::]:
            csv_table.append({
                'customer': obj[0],
                'item': obj[1],
                'total': obj[2],
                'quantity': obj[3],
                'date': obj[4],
            })
        return csv_table
