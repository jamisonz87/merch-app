from django.urls import path
from . import views

urlpatterns = [
    path('add_product/', views.add_product, name='add_product'),
    path('', views.index, name='admin_index'),
    path('view_order/<int:order_id>', views.view_order, name='view_order'),
]