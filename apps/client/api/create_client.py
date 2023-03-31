from rest_framework.generics import CreateAPIView
from apps.client.models import Client
from apps.client.serializers import ClientSerializer


class ClientCreateAPIView(CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
