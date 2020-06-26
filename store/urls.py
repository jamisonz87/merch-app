from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('', views.index, name='index'),
    path('view_product/<int:product_id>', views.view_product, name='view_product'),
    path('remove_from_cart/<int:product_index>', views.remove_from_cart, name='remove_from_cart'),
    path('add_to_cart/<int:item_id>',views.add_to_cart, name='add_to_cart'),
]