from rest_framework.generics import RetrieveAPIView
from apps.client.models import Client
from apps.client.serializers import ClientSerializer


class ClientRetrieveAPIView(RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
