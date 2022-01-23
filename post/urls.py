from django.urls import path
from .views import CategoryListView, CategoryDetailsView, ProductDetailsView

urlpatterns = [
    path('product/<int:pk>', ProductDetailsView.as_view(), name='product_details'),
    path('category/<int:pk>', CategoryDetailsView, name='category_details'),
    path('', CategoryListView.as_view(), name='home'),
]