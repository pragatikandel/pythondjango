from django.urls import path

from shop.views import HomeView, ProductView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('product/<str:product_slug>', ProductView.as_view(), name='product_page')
]
