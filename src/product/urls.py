from django.urls import path
from .views import all_products, one_product


urlpatterns = [
    path('', all_products, name='all_products'),
    # path('one_product/<int:pro_id>', one_product, name='one_product')
    path('one_product/<slug:slug>', one_product, name='one_product')
]


