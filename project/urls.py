from django.contrib import admin
from django.urls import path, include
from restapi import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api', views.index, name='index'),
    path('api/suppliers', views.SupplierList.as_view(), name='supplier-list'),
    path('api/suppliers/<int:pk>', views.SupplierDetail.as_view(), name='supplier-detail'),
    path('api/products', views.ProductList.as_view(), name='product-list'),
    path('api/products/<int:pk>', views.ProductDetail.as_view(), name='product-detail'),
    path('api/orders', views.OrderList.as_view(), name='order-list'),
    path('api/orders/<int:pk>', views.OrderDetail.as_view(), name='order-detail'),
    path('api/orders/<int:pk>/items', views.OrderItemCreate.as_view(), name='order-item'),
    path('api/orders/<int:pk>/items/<int:item>', views.OrderItemDetail.as_view(), name='order-item-detail'),
    path('api/token/', TokenObtainPairView.as_view(), name='token'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='refresh-token'),
    path('api/api-auth/', include('rest_framework.urls')),

]

urlpatterns = format_suffix_patterns(urlpatterns)
