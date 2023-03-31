from rest_framework.generics import ListAPIView
from apps.client.models import Client
from apps.client.serializers import ClientSerializer


class ClientListAPIView(ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
