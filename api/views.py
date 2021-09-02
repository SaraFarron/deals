import csv
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from .models import Deal, Client, Gem
from .serializers import ClientSerializer


class Home(APIView):
    parser_classes = [MultiPartParser]

    def get(self, request):
        for obj in [deal for deal in Deal.objects.all()]:
            if obj.item not in obj.customer.gems.all():
                obj.customer.gems.add(obj.item)
            obj.customer.money_spent += obj.total
            obj.customer.save()

        queryset = Client.objects.order_by('-money_spent')[:5]
        gems_list = []
        for client in queryset:
            gems_list += [gem for gem in client.gems.all()]

        for client in queryset:
            i = 0
            gems = client.gems.all()
            while i < len(gems):
                if gems_list.count(gems[i]) == 1:
                    client.gems.remove(gems[i])
                    client.save()
                i += 1

        serializer = ClientSerializer(data=queryset, many=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=200)

    def post(self, request, format=None):
        content_type = request.content_type.split(';')[0].strip()

        if content_type == 'multipart/form-data':
            try:
                fh = request.data.get('deals', None)
                csv_table = self.parse(fh)
            except AttributeError:
                return Response(
                    {'Ошибка:': 'Не найден csv файл'},
                    status=400
                )
            self.clean_data()
            self.create_objects(csv_table)
            return Response(status=200)
        else:
            return Response(
                {'Ошибка:': 'Неподдерживаемый формат данных, ожидался content-type: multipart/form-data'},
                status=400
            )

    def parse(self, stream):
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

            all_gems = Gem.objects.all()
            if obj['item'] not in [gem.name for gem in all_gems]:
                gem = Gem.objects.create(
                    name=obj['item']
                )
                gem.save()

            all_clients = Client.objects.all()
            if obj['customer'] not in [client.username for client in all_clients]:
                client = Client.objects.create(
                    username=obj['customer'],
                )
                client.save()

            deal = Deal.objects.create(
                customer=Client.objects.get(username=obj['customer']),
                item=Gem.objects.get(name=obj['item']),
                total=obj['total'],
                quantity=obj['quantity'],
                date=obj['date'],
            )
            deal.save()

    def clean_data(self):
        Deal.objects.all().delete()
        Client.objects.all().delete()
        Gem.objects.all().delete()
