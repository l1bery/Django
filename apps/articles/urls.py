from django.urls import path
from .views import home, shop, product, contact ,review_list

urlpatterns = [
    path('', home, name='home'),
    # path('home/', home, name='home'),
    path('shop/', shop, name='shop'),
    path('product/', product, name='product'),
    path('contact/', contact, name='contact'),
    path('reviews/',review_list,name = 'reviews')
]