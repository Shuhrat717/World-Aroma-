from django.urls import path

from apps.product.api.product_create import ProductCreatAPIView
from apps.product.api.product_list import ProductListAPIView
from apps.product.api.product_retrieve import ProductRetrieveAPIView
from apps.product.api.product_destroy import ProductDestroyAPIView

urlpatterns = [
    path('create/', ProductCreatAPIView.as_view()),
    path('list/', ProductListAPIView.as_view()),

    path('retrieve/<str:pk>/', ProductRetrieveAPIView.as_view()),
    path('destroy/<str:pk>/', ProductDestroyAPIView.as_view()),
]
