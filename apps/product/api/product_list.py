from rest_framework.generics import ListAPIView
from apps.product.models import Product
from apps.product.serializers import ProductSerializer


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
