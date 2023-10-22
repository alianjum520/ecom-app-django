from django.urls import path
from . import views





urlpatterns = [
 path('',views.Home,name='index'),
 path('category_view/<slug:slug>',views.CategoryView,name='CategoryView'),
 path('product_view/<int:id>',views.ProductView,name='ProductView'),
 path('about/',views.about,name='about'),
 path('contact/',views.contact,name='contact'),
 #path('search/',views.SearchView,name='SearchView'),

 
]