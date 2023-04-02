from rest_framework.generics import DestroyAPIView
from apps.product.models import Product
from apps.product.serializers import ProductSerializer


class ProductDestroyAPIView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
