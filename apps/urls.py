from django.urls import path, include

urlpatterns = [
    path('client/', include('apps.client.urls')),
    path('product/', include('apps.product.urls')),
]
