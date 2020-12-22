from django.urls import path
from .views import  list_products, delete_product, edit_product

urlpatterns = [
    path('', list_products, name="list_products"),
    path('delete/<int:pk>', delete_product, name="delete_product"),
    path('edit/<int:pk>', edit_product, name="edit_product"),
]
