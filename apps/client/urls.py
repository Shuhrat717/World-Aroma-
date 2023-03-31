from django.urls import path

from apps.client.api.create_client import ClientCreateAPIView
from apps.client.api.list_client import ClientListAPIView
from apps.client.api.retrieve_client import ClientRetrieveAPIView

urlpatterns = [
    path('create/', ClientCreateAPIView.as_view()),
    path('list/', ClientListAPIView.as_view()),

    path('retrieve/<str:pk>/', ClientRetrieveAPIView.as_view()),
]
