from django.urls import path
from . import views

urlpatterns = [
    path('update_item/',views.update_item,name='update_item'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('process_order/',views.processOrder,name='process_order')

]