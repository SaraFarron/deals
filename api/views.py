import csv
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from .models import Deal
from .serializers import DealSerializer


class Home(APIView):
    parser_classes = [MultiPartParser]

    def get(self, request):
        queryset = Deal.objects.order_by('-total')[:5]
        serializer = DealSerializer(data=queryset, many=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=200)

    def post(self, request, format=None):
        content_type = request.content_type.split(';')[0].strip()

        if content_type == 'text/csv':
            data = request.data
            csv_table = self.parse(data)
            self.create_objects(csv_table)
            return Response(status=200)

        elif content_type == 'multipart/form-data':
            try:
                fh = request.data.get('deals', None)
                csv_table = self.parse(fh)
            except AttributeError:
                return Response(
                    {'Status: Error, Desc:': 'Ошибка в имени аргумента, поменяйте на deals'},
                    status=400
                )
            self.create_objects(csv_table)
            return Response(status=200)
        else:
            return Response({'Status: Error, Desc:': 'Неподдерживаемый формат файла'}, status=415)

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

    def create_objects(self, list_of_deals):
        for obj in list_of_deals[1::]:
            deal = Deal.objects.create(
                customer=obj['customer'],
                item=obj['item'],
                total=obj['total'],
                quantity=obj['quantity'],
                date=obj['date'],
            )
            deal.save()
