from rest_framework.response import Response
from rest_framework.views import APIView


class Home(APIView):
    def get(self, request):
        return Response({'is_this': 'working?'})

    def post(self, request):
        pass
