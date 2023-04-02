from rest_framework.generics import RetrieveAPIView
from apps.product.models import Product
from apps.product.serializers import ProductSerializer


class ProductRetrieveAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
