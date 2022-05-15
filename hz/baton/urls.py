from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    # path('category/<str:slug>/', get_category, name='category'),
    path('category/<str:slug>/', Categories.as_view(), name='category'),
    # path('product/<str:slug>/', GetProduct.as_view(), name='product'),
    path('<int:id>/<slug:slug>/', get_product, name='product'),
    # path('shop/', Shop.as_view(), name='shop'),
    path('shop/', shop, name='shop'),
    path('feedback/', contacts, name='feedback'),
]
