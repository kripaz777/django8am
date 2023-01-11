from .views import *
from django.urls import path

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/<slug>', CategoryView.as_view(), name='category'),
    path('brand/<slug>', BrandView.as_view(), name='brand'),
    path('detail/<slug>', ProductDetailView.as_view(), name='detail'),
    path('signup', signup, name='signup'),
    path('search', SearchView.as_view(), name='search'),
    path('product_review/<slug>', product_review, name='product_review'),
    path('add_to_cart/<slug>', add_to_cart, name='add_to_cart'),
    path('reduce_cart/<slug>', reduce_cart, name='reduce_cart'),
    path('delete_cart/<slug>', delete_cart, name='delete_cart'),
    path('cart', CartView.as_view(), name='cart'),
]