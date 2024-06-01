from django.urls import path

from apps.base.views import (ProductListApiView, ProductCreateApiView,
ProductUpdateApiView, ProductDestroyAPIView, ProductRetrieveAPIView)
urlpatterns = [
    path('product/', ProductListApiView.as_view(), name='api_product'),
    path('product/create/', ProductCreateApiView.as_view(), name='api_product_create'),
    path('product/update/', ProductUpdateApiView.as_view(), name='api_product_update'),
    path('product/destroy/', ProductDestroyAPIView .as_view(), name='api_product_destroy'),
    path('product/<int:pk>/', ProductRetrieveAPIView.as_view(), name='api_product'),
    
]