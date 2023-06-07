from django.urls import path
from .views import *

urlpatterns = [
    path('manage', HomePageView.as_view(), name='admin'),

    path('manage/category', CategoryListView.as_view(), name="category"),
    path('manage/category/new', CategoryCreateView.as_view(), name="category_new"),
    path('manage/category/<int:pk>/delete/', CategoryDeleteView.as_view(), name="category_delete"),

    path('manage/product', ProductListView.as_view(), name="product"),
    path('manage/product/new', ProductCreateView.as_view(), name="product_new"),
    path('manage/product/<int:pk>/delete/', ProductDeleteView.as_view(), name="product_delete"),

    path('manage/city', CityListView.as_view(), name="city"),
    path('manage/city/new', CityCreateView.as_view(), name="city_new"),
    path('manage/city/<int:pk>/delete/', CityDeleteView.as_view(), name="city_delete"),

    path('manage/inventory', InventoryListView.as_view(), name="inventory"),
    path('manage/inventory/new', InventoryCreateView.as_view(), name="inventory_new"),
    path('manage/inventory/<int:pk>/delete/', InventoryDeleteView.as_view(), name="inventory_delete"),

    path('manage/inventoryProduct', InventoryProductListView.as_view(), name="inventoryProduct"),
    path('manage/inventoryProduct/new', InventoryProductCreateView.as_view(), name="inventoryProduct_new"),
    path('manage/inventoryProduct/<int:pk>/delete/', InventoryProductDeleteView.as_view(), name="inventoryProduct_delete"),

    path('manage/order', OrderListView.as_view(), name="order"),
    path('manage/order/<int:pk>/update/', OrderUpdateView.as_view(), name="order_update"),
    path('manage/order/<int:pk>/delete/', OrderDeleteView.as_view(), name="order_delete"),

    path('', UserProductListView.as_view(), name='home'),
    path('userOrder/<int:pk>', userOrder, name="userOrder"),
    path('orderList', UserOrderListView.as_view(), name='orderList'),
]
