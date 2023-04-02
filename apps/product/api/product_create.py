from rest_framework.generics import CreateAPIView
from apps.product.models import Product
from apps.product.serializers import ProductSerializer


class ProductCreatAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
