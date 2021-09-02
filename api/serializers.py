from rest_framework.serializers import ModelSerializer, StringRelatedField
from .models import Client


class ClientSerializer(ModelSerializer):
    gems = StringRelatedField(many=True)

    class Meta:
        model = Client
        fields = ['username', 'money_spent', 'gems']
