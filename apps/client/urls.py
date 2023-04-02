from django.urls import path

from apps.client.api.client_create import ClientCreateAPIView
from apps.client.api.client_list import ClientListAPIView
from apps.client.api.client_retrieve import ClientRetrieveAPIView

urlpatterns = [
    path('create/', ClientCreateAPIView.as_view()),
    path('list/', ClientListAPIView.as_view()),

    path('retrieve/<str:pk>/', ClientRetrieveAPIView.as_view()),
]
