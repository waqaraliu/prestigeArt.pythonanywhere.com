from django.urls import path
from .views import HomeView
from .views import ProductsListView
from .views import ProductDetailView


urlpatterns = [
    #path('', HomeView.as_view(), name='home'),
    path('', ProductsListView.as_view(), name='home'),
    path('category/<int:pk>', ProductDetailView.as_view(), name='category_list'),
]
